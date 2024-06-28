import math


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        page_no = 0
        for page in self.photos:
            page_no += 1
            current_photos = len(page)

            if current_photos != 4:
                page.append(f"{label}")
                return f"{label} photo added successfully on page {page_no} slot {current_photos + 1}"

        return "No more free slots"

        # на Дидо решението:
        # for page in range(self.pages):
        #     if len(self.photos[page]) < PhotoAlbum.PHOTOS_PER_PAGE:
        #         self.photos[page].append(label)
        #         return f"{label} photo added successfully on page {page+1} slot {len(self.photos[page])}"
        #
        # return "No more free slots"

    def display(self) -> str:
        result = "-" * 11 + "\n"

        for page in self.photos:
            result += ("[] " * len(page)).rstrip() + "\n"   # гърми в judge заради спейс в дясно
                                                            # и за това се позлва .rstrip()
            result += "-----------\n"

        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
