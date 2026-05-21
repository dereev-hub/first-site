from sdk.genius_api import search_by_text


class SearchService:
    #  TODO: метод поиска треков по тексту, создать новый роутер и контроллер к этому сервису что бы его использовать в след раз с фронта, ориентируясь на другие контроллеры( тест в бруно )
    def search_tracsk_by_text(self, text: str):
        return search_by_text(text)