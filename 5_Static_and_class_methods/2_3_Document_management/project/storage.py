from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = next(filter(lambda categ: categ.id == category_id, self.categories))
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        # topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        # document = next(filter(lambda doc: doc.id == document_id, self.documents))
        self.get_document(document_id).file_name = new_file_name

    def delete_category(self, category_id: int) -> None:
        category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        # document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(self.get_document(document_id))

    def get_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        return document

    def __repr__(self) -> str:
        # result = ""
        # for doc in self.documents:
        #     result += repr(doc) + "\n"
        # return result

        return "\n".join(str(d) for d in self.documents)
