from unittest import TestCase

from project.gallery import Gallery


class TestGallery(TestCase):
    def setUp(self):
        self.gallery = Gallery("name", "city", 5.5, True)
        self.gallery.exhibitions = {"test": 1, "test2": 2}

    def test_object_is_initialised(self):
        self.assertEqual(self.gallery.gallery_name, "name")
        self.assertEqual(self.gallery.city, "city")
        self.assertEqual(self.gallery.area_sq_m, 5.5)
        self.assertEqual(self.gallery.open_to_public, True)
        self.assertEqual(self.gallery.exhibitions, {"test": 1, "test2": 2})

    def test_gallery_name_getter(self):
        self.gallery.gallery_name = "NewName"
        self.assertEqual(self.gallery.gallery_name, "NewName")

    def test_gallery_name_setter(self):
        with self.assertRaises(Exception) as ex:
            self.gallery.gallery_name = "Wrong Name!"

        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_gallery_city_getter(self):
        self.gallery.city = "New City"
        self.assertEqual(self.gallery.city, "New City")

    def test_gallery_city_setter(self):
        with self.assertRaises(Exception) as ex:
            self.gallery.city = "!!!Wrong City"

        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_gallery_area_sq_m_getter(self):
        self.gallery.area_sq_m = 500
        self.assertEqual(self.gallery.area_sq_m, 500)

    def test_gallery_area_sq_m_setter(self):
        with self.assertRaises(Exception) as ex:
            self.gallery.area_sq_m = -5

        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition_existing(self):
        res = self.gallery.add_exhibition("test", 1)

        self.assertEqual('Exhibition "test" already exists.', res)
        self.assertEqual(self.gallery.exhibitions, {"test": 1, "test2": 2})


    def test_add_exhibition_new(self):
        res = self.gallery.add_exhibition("test3", 3)

        self.assertEqual(res, 'Exhibition "test3" added for the year 3.')
        self.assertEqual(self.gallery.exhibitions, {"test": 1, "test2": 2, "test3": 3})

    def test_remove_exhibition_not_found(self):
        res = self.gallery.remove_exhibition("test3")

        self.assertEqual(res, 'Exhibition "test3" not found.')
        self.assertEqual(self.gallery.exhibitions, {"test": 1, "test2": 2})

    def test_remove_exhibition_successfully(self):
        res = self.gallery.remove_exhibition("test")

        self.assertEqual(res, 'Exhibition "test" removed.')
        self.assertEqual(self.gallery.exhibitions, {"test2": 2})

    def test_list_exhibitions_open_to_public(self):
        self.gallery.open_to_public = True
        self.assertEqual(f"test: 1\ntest2: 2",
                                   self.gallery.list_exhibitions())

    def test_list_exhibitions_closed_to_public(self):
        self.gallery.open_to_public = False
        self.assertEqual(
            f'Gallery {self.gallery.gallery_name} is currently closed for public! Check for updates later on.',
            self.gallery.list_exhibitions()
        )

if __name__ == "__main__":
    main()