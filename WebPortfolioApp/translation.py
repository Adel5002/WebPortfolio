from .models import PortfolioStructure
from modeltranslation.translator import register, \
    TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться


# регистрируем наши модели для перевода

@register(PortfolioStructure)
class PortfolioStructureTranslationOptions(TranslationOptions):
    fields = ('title', 'descr')  # указываем, какие именно поля надо переводить в виде кортежа


