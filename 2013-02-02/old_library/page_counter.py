def checkio(data):
    'return the number of pages'
    
    height = data['height']
    width = data['width']
    text = data['text']
    import math
    lines = math.ceil(len(" ".join(text.split()))/(height*width)) + text.count('\n')
    if lines == 0:
        return 1
    return lines 
    
    
if __name__ == '__main__':
    assert checkio({'height':3,
             'width':5,
             'text': 'To be or not to be'
    }) == 2 , 'From description'
    
    assert checkio({'height':1,
             'width':5,
             'text': 'HI'
    }) == 1, 'with single sort word'
    
    assert checkio({'height':1,
             'width':5,
             'text': 'hello'
    }) == 1, 'with signle word with long as width'
    
    assert checkio({'height':3,
             'width':5,
             'text': ''
    }) == 1, 'one page for no words'
    
    assert checkio({'height':3,
             'width':5,
             'text': 'It\'s boooooooorrrrrrriiiiiinnnnggggg dude'
    }) == 3, 'With a one long word'
    
    assert  checkio({'height':3,
             'width':5,
             'text': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Cras hendrerit enim ultricies justo tincidunt ut auctor ipsum hendrerit. Phasellus ultricies dolor eu arcu auctor a rutrum enim tristique. 
Phasellus purus odio, pharetra in sodales vel, adipiscing eget libero. Quisque rhoncus urna at ipsum tincidunt facilisis. In vitae diam dolor. 
Nullam eleifend aliquam porttitor. Curabitur viverra malesuada eleifend. Fusce eu dui quis neque accumsan consectetur id id metus. 
Cras rutrum purus sed massa malesuada in consequat augue viverra. Vestibulum consectetur lacinia commodo. 
Phasellus urna nisi, tincidunt a ullamcorper egestas, iaculis sed mauris.'''
    }) == 49 , 'Lorem ipsum'
    
    print('All ok :)')
