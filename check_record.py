class Sol:
    def check_record(self,s):
        num_of_as=0
        for i in range(len(s)):
            if s[i]=='A':
                num_of_as+=1
                if num_of_as>1:
                    return False
            elif s[i]=='L':
                if i<=len(s)-3 and s[i:i+3]=='LLL':
                    return False
        return True
