class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0  # Initialize two pointers, one for name and one for typed
        
        while j < len(typed):  # Traverse the entire typed string
            if i < len(name) and name[i] == typed[j]:  
                # If characters match, move both pointers
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:  
                # If characters don't match but it's a valid long press, move only j
                j += 1
            else:
                # If characters don't match and it's not a long press, return False
                return False
        
        # After loop, check if all characters of name were matched
        return i == len(name)
