"""This is an example of working with areas module."""
import areas
import inspect
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

classes = [name for name, obj in inspect.getmembers(areas, inspect.isclass)]


while True:
    print('This script calculates parameters only for this list of shapes:')
    for i in range(len(classes)):
        print(i+1, '. ', classes[i] , sep='')
    print("\nSelect one of them by typing it's name or number.")
    print("Or write 'quit' to exit.")
    
    user_input = input('Selected shape: ').lower()
    exit_words_list = ['q', 'quit', 'exit', '0']
    
    if user_input in exit_words_list:
        break
    elif (user_input.capitalize() in classes) \
         or (user_input.isdigit() and int(user_input) in range(1, len(classes)+1)):

        if user_input.isdigit():
            class_name = classes[int(user_input)-1]
        else:
            class_name = user_input.capitalize()
            
        class_ = getattr(areas, class_name)
        annotations = inspect.getfullargspec(class_).annotations
        args = [i for i in inspect.getfullargspec(class_).args if i != 'self']
        
        print('\nThe', class_name.lower(), 'needs this values:')
        if len(annotations) == len(args):
            for req in annotations:
                print(req.capitalize(), 'with this type(s): ', end='')
                for letter in str(annotations[req]):
                    print(letter if letter != '|' else 'or' , sep='', end='')
                print()
        else:
            for arg in args:
                print(arg.capitalize())
                
        print('\nPut values here:')
        user_args = []
        for arg in args:
            print(arg.capitalize(), ': ', sep='', end='')
            user_args.append(float(input()))

        instanse_of_shape = class_(*user_args)
        clear_screen()
        print('Measures of your ', class_name.lower(), ':', sep='')
        
        shape_measures = instanse_of_shape.__dict__
        shape_measures_max_len = max([len(i) for i in shape_measures])
        for shape_measure in shape_measures:
            _shape_measure = (shape_measure+':').ljust(shape_measures_max_len+1).capitalize()
            print(_shape_measure, shape_measures[shape_measure])
    
        input('\nPress enter to continue.')
        
        print('\n')
    else:
        clear_screen()
        print('ERROR: There is no figure with this type or id.')
        print()