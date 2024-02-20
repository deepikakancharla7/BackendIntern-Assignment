Project Overview This project aims to create a REST API using Django Rest Framework for storing paragraphs and their associated words in a PostgreSQL database. The API provides endpoints for user authentication, CRUD operations for paragraphs and words, as well as word search functionality.

Code Preparation Custom User Model CustomUser model: Subclass of Django's AbstractBaseUser providing custom user model with fields email, name, dob, created_at, and modified_at.

Paragraph and Word Models Paragraph model: Represents a paragraph with fields content, created_at, modified_at, and a foreign key user to link to the CustomUser who created it. Word model: Represents a word within a paragraph with a field word and a foreign key paragraph to associate it with a specific paragraph.

Serializers CustomUserSerializer: Serializes CustomUser model for API representation. ParagraphSerializer: Serializes Paragraph model for API representation. WordSerializer: Serializes Word model for API representation.

Views CustomUserViewSet: Viewset for CRUD operations on CustomUser model. ParagraphViewSet: Viewset for CRUD operations on Paragraph model. WordViewSet: Viewset for CRUD operations on Word model. WordSearchView: View to search for paragraphs containing a specific word.

Authentication API Token Authentication: Token-based authentication for user authentication using Django Rest Framework's TokenAuthentication.

URL Routing URL Configuration: Defines URL patterns for routing requests to appropriate views.

Conclusion This documentation provides an overview of how the code is prepared for the project, including models, serializers, views, authentication, and URL routing. With this setup, the project aims to provide a robust and scalable REST API for storing paragraphs and words in a PostgreSQL database.
