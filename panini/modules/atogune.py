'''पदच्छेदः  अतः ( पञ्चमी-एकवचनम् ) , गुणे ( सप्तमी-एकवचनम् )
अनुवृत्तिः  अचि ६.१.७७ , पररूपम् ६.१.९४ , अपदान्तात् ६.१.९६
अधिकारः  संहितायाम् ६.१.७२ , एकः पूर्वपरयोः ६.१.८४
अनुवृत्तिसहितं सूत्रम्  अपदान्तात् अतः गुणे पूर्वपरयोः एकः पररूपम्'''
print('अपदान्त-अकारात् गुणे परे संहितायाम् पूर्वपरयोः एकः पररूप-एकादेशः भवति ')
print('''In the context of संहिता, when an अपदान्त अकार is followed by 
a गुण letter, both of them are replaced by a single पररूप.''')

def modify_list(Modified_Cleaned_Strings):
    if Modified_Cleaned_Strings[1][-1] == 'अ' and Modified_Cleaned_Strings[2][0] in ['अ', 'ए', 'ओ']:
        new_list = [Modified_Cleaned_Strings[0], Modified_Cleaned_Strings[1][:-1], Modified_Cleaned_Strings[2]]
        return new_list
    else:
        return Modified_Cleaned_Strings
#Modified_Cleaned_Strings = ['प्अच्', 'अ', 'अन्त्इ']
#new_list = modify_list(Modified_Cleaned_Strings)
#print("New List:", new_list)
