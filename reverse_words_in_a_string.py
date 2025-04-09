# 151. Reverse Words in a String

def reverseWords(s: str) -> str:

    return " ".join(s.split()[::-1])


if __name__ == "__main__":
    print(reverseWords("the sky is blue"))