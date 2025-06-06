#姓名：王薪洋，学号：24210227016，日期，25.6.6
class VocabularyBook:
    def __init__(self):
        self.words = {}

    def display_words(self):
        if not self.words:
            print("生词本内容为空")
        else:
            for word, translation in self.words.items():
                print(f"{word}: {translation}")

    def study_word(self):
        if not self.words:
            print("生词本内容为空")
            return
        word = list(self.words.keys())[0]
        translation = input(f"请输入 '{word}' 的翻译: ")
        if translation == self.words[word]:
            print("太棒了")
        else:
            print("再想想")

    def add_word(self):
        new_word = input("请输入新单词: ")
        new_translation = input("请输入翻译: ")
        if new_word in self.words:
            print("此单词已存在")
        else:
            self.words[new_word] = new_translation
            print("单词添加成功")

    def delete_word(self):
        self.display_words()
        word = input("请输入要删除的单词: ")
        if word in self.words:
            del self.words[word]
            print("删除成功")
        else:
            print("删除的单词不存在")

    def clear_words(self):
        if not self.words:
            print("生词本内容为空")
        else:
            self.words.clear()
            print("生词本已清空")

    def exit_book(self):
        print("退出生词本")
        exit()

def main():
    vocab_book = VocabularyBook()
    while True:
        print("\n请选择操作：")
        print("1. 查看生词列表")
        print("2. 背单词")
        print("3. 添加新单词")
        print("4. 删除单词")
        print("5. 清空生词本")
        print("6. 退出生词本")
        choice = input("请输入选项（1-6）: ")

        if choice == '1':
            vocab_book.display_words()
        elif choice == '2':
            vocab_book.study_word()
        elif choice == '3':
            vocab_book.add_word()
        elif choice == '4':
            vocab_book.delete_word()
        elif choice == '5':
            vocab_book.clear_words()
        elif choice == '6':
            vocab_book.exit_book()
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()