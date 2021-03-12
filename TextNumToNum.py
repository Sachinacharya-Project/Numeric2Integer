numberlist = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "hundred": 100,
    "thousand": 1000,
}
class Word_To_Number():
    def __sum_asf__(self, arr):
        arr = list(arr)
        pro_arr = arr.copy()
        if 'and' in pro_arr:
            pro_arr.remove('and')
        condition = True
        for item in pro_arr:
            if str(item).isdigit():
                condition = True
            else:
                condition = False
                break
        if condition:
            summ = 0
            for item in pro_arr:
                summ = item + summ
            return summ
        else:
            return arr

    def __filteration_number__(self, arr):
        final_array = []
        added_things = []
        for item in list(arr):
            master = ''
            try:
                master = str(item).isdigit()
            except Exception:
                master = False
            if master:
                item = int(item)
                if item %1000 == 0 or item % 100 == 0 or item%10 == 0:
                    index = arr.index(item)
                    if item%10==0 and item%100 != 0 and item%1000 != 0:
                        if index >= len(arr) - 1:
                            final_array.append(item)
                        else:
                            if str(arr[index + 1]).isdigit():
                                added_things.append(arr[index + 1])
                                final_array.append(item + int(arr[index + 1]))
                            else:
                                final_array.append(item)
                    else:
                        if index <= 0:
                            final_array.append(item)
                        else:
                            if str(arr[index - 1]).isdigit():
                                added_things.append(arr[index - 1])
                                final_array.append(item * int(arr[index - 1]))
                            else:
                                final_array.append(item)
                else:
                    final_array.append(item)
            else:
                final_array.append(item)
        for item in final_array:
            if item in added_things:
                final_array.remove(item)
        return self.__sum_asf__(final_array)
    def word_to_number(self, word):
        """
        Main Function\n
        Receives String of Numeric as well as integer and converts them into regular interger and returns it.
        """
        word = str(word)
        word_list = word.split(' ')
        result_array = []
        for words in word_list:
            if words.lower().endswith('ty'):
                words = words.replace('ty', '')
                excepted = ['twen', 'thir', 'fif']
                number_expected = [2, 3, 5]
                if words in excepted:
                    astrisk = str(number_expected[excepted.index(words.lower())])
                else:
                    astrisk = str(numberlist.get(words.lower(), words))
                if astrisk.isdigit():
                    astrisk = int(astrisk) * 10
                    result_array.append(astrisk)    
            else: 
                astrisk = numberlist.get(words.lower(), words)
                if str(astrisk).isdigit():
                    result_array.append(int(astrisk))
                else:
                    result_array.append(astrisk)
        stringReturn = ""
        for item in self.__filteration_number__(result_array):
            stringReturn += str(item)+ " "
        return stringReturn