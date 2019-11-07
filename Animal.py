class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        num_limbs = self.arms + self.legs
        return num_limbs


def main():
    spider = Animal(4, 4)
    spidlimbs = spider.limbs()
    print(spidlimbs)


if __name__ == "__main__":
    main()

