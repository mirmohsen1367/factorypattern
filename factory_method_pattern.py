
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describ(self):
        pass


class PersonalSection(Section):

    def describ(self):
        print("personal section")


class AlbumSection(Section):

    def describ(self):
        print("album section")


class PatnetSection(Section):

    def describ(self):
        print("patnet section")


class PublicationSectionz(Section):

    def describ(self):
        print("publication section")


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = []
        self.createprofile()

    @abstractmethod
    def createprofile(self):
        pass

    def getsection(self):
        return self.sections

    def addsection(self, section):
        self.sections.append(section)


class Facebook(Profile):

    def createprofile(self):
        self.addsection(PersonalSection())
        self.addsection(AlbumSection())


class Linkdin(Profile):

    def createprofile(self):
        self.addsection(PersonalSection())
        self.addsection(PatnetSection())
        self.addsection(PublicationSectionz())


if __name__ == "__main__":
    object_type = input("please ebter the type of social Linkdin or Facebook?")
    profile = eval(object_type)()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getsection())

