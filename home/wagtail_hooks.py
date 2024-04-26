# from home.models import Project
# from wagtail.snippets.models import register_snippet
# from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
# from wagtail.admin.ui.tables import UpdatedAtColumn
# from wagtail.admin.panels import (
#     FieldPanel,
#     ObjectList,
#     TabbedInterface,
# )


# class ProjectsSnippetViewSet(SnippetViewSet):
#     model = Project
#     menu_label = "Projects"
#     menu_icon = "image"
#     list_display = ("title",)
#     edit_handler = TabbedInterface(
#         [
#             ObjectList(
#                 [
#                     FieldPanel("title"),
#                     FieldPanel("description"),
#                     FieldPanel("images"),
#                 ],
#                 heading="Details",
#             ),
#         ]
#     )



# class MenuGroup(SnippetViewSetGroup):
#     menu_label = "Projects"
#     menu_icon = "tag"
#     menu_order = 200
#     items = (ProjectsSnippetViewSet,)


# register_snippet(MenuGroup)
