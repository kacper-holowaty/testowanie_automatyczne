class hamming:
    @staticmethod
    def distance(strand1, strand2):
        if len(strand1) > len(strand2):
            raise ValueError("Dane po lewej są dłuższe!")

        elif len(strand1) < len(strand2):
            raise ValueError("Dane po prawej są dłuższe!")
        
        else:
            counter=0
            for i in range(0, len(strand1)):
                if strand1[i] != strand2[i]:
                    counter+=1
        return counter
    