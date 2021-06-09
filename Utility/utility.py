def isElementOf(liste, cat_attr, attr):
    """
        lets you know if attr is a value of cat_attr
    """
    capt = False
    for value in liste:
        if value[0] == cat_attr:
            for attr_object in value[1]:
                if attr_object.getName() == attr:
                    capt = True

    return capt


def ListOfAttributeExceptWord(liste, word="Play"):
    """
       returns the list of attributes without the Play class
    """
    copy_attri = list()
    for value in liste:
        if value[0] != word:
            copy_attri.append(value)

    return copy_attri


def deleteFrom(liste, begin):
    """
        delete from beguin to the end o the liste
    """
    for value in liste[begin:]:
        liste.remove(value)
