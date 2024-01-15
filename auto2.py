import re

def message_probability(user_message, recognized_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = set()

    message_certainty = sum(1 for word in user_message if word in recognized_words)
    percentage = message_certainty / len(recognized_words) if recognized_words else 0

    has_required_words = all(word in user_message for word in required_words)

    return int(percentage * 100) if has_required_words or single_response else 0

def check_all_messages(message):
    responses = [
        ('I recommend taking your car to a professional mechanic for a thorough inspection.', {'inspection', 'mechanic', 'professional', 'check'}, True, set()),
        ('If your car is not starting, it might be a battery issue. Check the battery connection, charge, and fuel level before attempting to start again.', {'car', 'not starting', 'battery', 'connection', 'charge', 'fuel'}, False, {'starting','not'}),
        ('Strange noises or warning lights may indicate an engine problem. Pay attention to any unusual sounds or dashboard warnings.', {'engine', 'noise', 'warning lights'}, False, {'noise'}),
        ('To improve handling, check tire pressure and condition regularly. Proper tire maintenance can prevent handling issues.', {'tire', 'pressure', 'handling', 'improve'}, False, {'handling'}),
        ('If your headlights are not turning on, it could be due to burned-out bulbs or power/ground issues. Inspect and fix accordingly.', {'headlight', 'not turning on', 'burned-out bulbs', 'power', 'ground'}, False, {'headlight','not'}),
        ('If your AC is not cooling or turning on, check refrigerant levels, clean the air filter, and inspect the compressor and condenser for issues.', {'ac', 'not cooling', 'not turning on', 'refrigerant', 'air filter', 'compressor', 'condenser'}, False, {'ac', 'cooling','not'}),
        ('Worn-out brakes can lead to slow stopping and unusual noises. Consider changing brake pads if you notice vibrations or odd sounds while braking.', {'car', 'stops slowly', 'brakes squeak', 'brake pads', 'vibrations'}, False, {'brakes'}),
        ('Transmission problems may cause jerking or hesitation during gear shifts. It is advisable to have the transmission checked for issues.', {'jerks', 'hesitates', 'hard to change gears', 'transmission', 'gear shifts'}, False, {'gears'}),
    ]
    responses += [
    ('If you notice a burning smell, it could be an overheating issue. Check the coolant levels and radiator for any leaks.', {'burning smell', 'overheating', 'coolant', 'radiator', 'leaks'}, False, {'burning', 'smell'}),
    ('A vibrating steering wheel may indicate an issue with the wheel balance or alignment. Consider getting a wheel alignment and balancing.', {'vibrating', 'steering wheel', 'wheel balance', 'alignment'}, False, {'vibrating' , 'steering wheel'}),
    ("A persistent check engine light could be signaling a problem with the vehicle's engine or emissions system. It's recommended to have the car's diagnostics checked.", {'check engine light', 'engine', 'emissions', 'diagnostics'}, False, {'light','engine' }),
    ('If your car pulls to one side while driving, it may be due to uneven tire wear or alignment issues. Check the tire tread and alignment.', {'car pulls', 'uneven tire wear', 'alignment issues', 'tire tread', 'alignment'}, False, {'car pulls', 'one side'}),
    ('For a fuel-efficient drive, ensure your tires are properly inflated, and the air filter is clean. Regular maintenance can improve fuel efficiency.', {'fuel-efficient drive', 'tire inflation', 'air filter', 'maintenance', 'fuel efficiency'}, False, {'fuel efficiency'}),
    ('If you experience a loss of power, it could be related to issues with the fuel system or air intake. Check the fuel pump and air filter for any problems.', {'loss of power', 'fuel system', 'air intake', 'fuel pump', 'air filter'}, False, {'power', 'loss'}),
    ('Unusual smells from the exhaust could indicate problems with the catalytic converter or exhaust system. Inspect for any visible damage or leaks.', {'unusual smells', 'exhaust', 'catalytic converter', 'exhaust system', 'visible damage', 'leaks'}, False, {'smell', 'exhaust'}),
    ]


    probabilities = {response: message_probability(message, words, single, required) for response, words, single, required in responses}

    best_match = max(probabilities, key=probabilities.get)

    return 'I\'m sorry, I don\'t have enough information to diagnose the issue.' if probabilities[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    user_input = input('You: ').strip()
    if not user_input:
        print("Bot: Please provide valid input.")
        continue  
    print('Bot: ' + get_response(user_input))
