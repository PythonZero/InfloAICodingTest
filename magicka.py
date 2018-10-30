class Magicka:

    def __main__(self, combine, oppose, elements):
        self.returned = self.invoke(combine, oppose, elements)

    @classmethod
    def invoke(cls, combine: str, oppose: str, elements: str) -> str:
        """
        :param combine:  str of 3 letters -> the first 2
                         combine to form the third
        :param oppose:   str: 2 letters, and they are opposed
        :param elements: inputted elements
        :return: resulting string
        """

        for letter in elements:
            cls._check_combine(elements, combine)
            cls._check_oppose(elements, oppose)

    @classmethod
    def iterator(cls, elements, oppose, combine):
        temp_list = ''
        while True:
            posn = 1
            temp_list = elements[posn] + elements[posn-1]
            cls._check_combine()


    @staticmethod
    def _check_oppose(elements, oppose):
        """
        :param elements: inputted elements
        :param oppose:  str of 3 letters -> the first 2
                         oppose to form the third
        :return:
        """
        oppose_letter1 = oppose[0]
        oppose_letter2 = oppose[1]
        
        loc_letter1 = None
        loc_letter2 = None
        
        for loc, letter in enumerate(elements):
            # TODO: change below into a for loop
            if (letter == oppose_letter1) and loc_letter1 is not None:
                loc_letter1 = loc
            if (letter == oppose_letter2) and (loc_letter2 is not None):
                loc_letter2 = None

    @staticmethod
    def _check_combine(elements, combine):
        """
        :param elements: the last 2 letters of the elements
        :param combine: three letters, where letter 1 & 2 --> letter 3
        :return:
        """
        combine_letter1 = combine[0]
        combine_letter2 = combine[1]
        combined_letter = combine[2]

        if elements[0] is any([combine_letter1, combine_letter2]):
            return combined_letter
        return elements
