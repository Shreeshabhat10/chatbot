import re

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    response('I recommend taking your car to a professional mechanic for a thorough inspection.', ['problem', 'issue', 'car', 'fix', 'repair'], single_response=True)
    response('It might be a battery issue. Check if the battery is properly connected and charged. Also check the fuel level before trying again.', [ 'car', 'not starting'], required_words=['starting'])
    response('You may have a problem with the engine. Check for any strange noises or warning lights.', ['engine', 'noise'], required_words=[ 'noise'])
    response('Consider checking the tire pressure and condition. Low tire pressure can cause handling issues.', ['tire', 'pressure', 'handling'], required_words=['improve', 'handling'])
    response('This could be due to burned-out bulbs, or an issue with power or ground. Check for power and ground, and fix if necessary.', ['headlight',  'not turning on'], required_words=['headlight'])
    response('Check the refrigerent levels, check if the air filter is clogged and clean it regularly. Also check for faulty compressor and broken condenser.', ['ac', 'not cooling', 'not turning on'], required_words=['ac'])
    response('The brakes can become worn out, making it difficult to stop the car. If you notice any unusual noises or vibrations when you apply the brakes, it’s best to change the brake pads.', ['car', 'stops slowly', 'brakes squeaks'], required_words=['brakes'])
    response('Transmission problems can cause the car to jerk or hesitate when shifting gears. It is better to get it checked.', ['jerks', 'hesitates', 'hard to change gears'], required_words=['gears'])

    
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return 'I\'m sorry, I don\'t have enough information to diagnose the issue.' if highest_prob_list[best_match] < 1 else best_match

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