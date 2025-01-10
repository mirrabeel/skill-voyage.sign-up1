import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [(rank, suit) for suit in suits for rank in ranks]

rank_circle = {rank: i for i, rank in enumerate(ranks)}

def generate_hand():
    return random.sample(deck, 5)

def calculate_steps(start, end):
    start_pos = rank_circle[start]
    end_pos = rank_circle[end]
    steps = (end_pos - start_pos) % len(ranks)
    print(f"steps from {start} to {end}: {steps}")
    return steps

def encode_order(steps):
    orders = [
        ('small', 'medium', 'large'),
        ('small', 'large', 'medium'),
        ('medium', 'small', 'large'),
        ('medium', 'large', 'small'),
        ('large', 'small', 'medium'),
        ('large', 'medium', 'small')
    ]
    if not (1 <= steps <= 6):  
        raise ValueError(f"invalid step count: {steps}")
    return orders[steps - 1]

def rank_order(cards):
    sorted_cards = sorted(cards, key=lambda card: rank_circle[card[0]])
    return {
        'small': sorted_cards[0],
        'medium': sorted_cards[1],
        'large': sorted_cards[2]
    }

def assistant_logic():
    hand = generate_hand()
    print("generated hand:", hand)
    
    suit_groups = {}
    for card in hand:
        suit_groups.setdefault(card[1], []).append(card)

    for suit, cards in suit_groups.items():
        if len(cards) >= 2:
            break
    else:
        raise ValueError("invalid hand")

    hidden_card = cards[1]  
    shown_card = cards[0]  

    steps = calculate_steps(shown_card[0], hidden_card[0])

    remaining_cards = [card for card in hand if card not in (hidden_card, shown_card)]
    ranked = rank_order(remaining_cards)

    order = encode_order(steps)
    ordered_cards = [ranked[order[0]], ranked[order[1]], ranked[order[2]]]

    print("hidden card:", hidden_card)
    print("shown card:", shown_card)
    print("ordered cards:", ordered_cards)
    return shown_card, ordered_cards, hidden_card

def illusionist_logic(shown_card, ordered_cards):
    suit = shown_card[1]

    orders = [
        ('small', 'medium', 'large'),
        ('small', 'large', 'medium'),
        ('medium', 'small', 'large'),
        ('medium', 'large', 'small'),
        ('large', 'small', 'medium'),
        ('large', 'medium', 'small')
    ]

    ranked = rank_order(ordered_cards)
    order_tuple = tuple(
        'small' if card == ranked['small'] else
        'medium' if card == ranked['medium'] else
        'large'
        for card in ordered_cards
    )

    steps = orders.index(order_tuple) + 1

    start_rank = shown_card[0]
    hidden_rank = ranks[(rank_circle[start_rank] + steps) % len(ranks)]

    hidden_card = (hidden_rank, suit)
    print("hidden card:", hidden_card)
    return hidden_card

try:
    shown_card, ordered_cards, hidden_card = assistant_logic()
    decoded_card = illusionist_logic(shown_card, ordered_cards)

    assert hidden_card == decoded_card, "trick failed!"
    print("decoded!")
except Exception as e:
    print("error:", e)
