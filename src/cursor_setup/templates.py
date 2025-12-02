"""
Template definitions for cursor-setup.

Each template contains expert-level .cursorrules content for specific tech stacks.
"""

TEMPLATES = {
    "python": {
        "name": "Python",
        "description": "Modern Python with type hints, docstrings, and best practices",
        "content": """# Python Development Rules

You are an expert Python developer. Follow these guidelines for all code generation.

## Code Style & Standards

- Follow PEP 8 style guide strictly
- Use 4 spaces for indentation, never tabs
- Maximum line length of 88 characters (Black formatter standard)
- Use snake_case for functions and variables
- Use PascalCase for class names
- Use SCREAMING_SNAKE_CASE for constants

## Type Hints (Required)

- Add type hints to ALL function signatures
- Use `from __future__ import annotations` for forward references
- Prefer built-in generics (list, dict) over typing module equivalents (Python 3.9+)
- Use `Optional[X]` or `X | None` for nullable types
- Use `TypeVar` for generic functions
- Example:
  ```python
  def process_items(items: list[str], count: int | None = None) -> dict[str, int]:
  ```

## Docstrings (Required)

- Use Google-style docstrings for all public functions, classes, and modules
- Include Args, Returns, Raises sections where applicable
- Example:
  ```python
  def calculate_total(items: list[float], tax_rate: float) -> float:
      \"\"\"Calculate the total price including tax.

      Args:
          items: List of item prices.
          tax_rate: Tax rate as a decimal (e.g., 0.08 for 8%).

      Returns:
          Total price including tax.

      Raises:
          ValueError: If tax_rate is negative.
      \"\"\"
  ```

## Error Handling

- Use specific exception types, never bare `except:`
- Create custom exceptions for domain-specific errors
- Use context managers for resource management
- Prefer EAFP (Easier to Ask Forgiveness than Permission) over LBYL

## Project Structure

- Use `src/` layout for packages
- Keep `__init__.py` files minimal
- Separate concerns: models, services, utils, etc.
- Use absolute imports within the project

## Testing

- Write tests using pytest
- Use fixtures for test setup
- Aim for descriptive test names: `test_should_raise_when_invalid_input`
- Use parametrize for testing multiple cases

## Dependencies

- Use virtual environments (venv or conda)
- Pin dependencies in requirements.txt or pyproject.toml
- Separate dev dependencies from production

## Modern Python Features

- Use f-strings for string formatting
- Use dataclasses or Pydantic for data structures
- Use pathlib for file paths
- Use enumerate() instead of manual indexing
- Use context managers (with statements) for resources
"""
    },

    "nextjs": {
        "name": "Next.js",
        "description": "Next.js 14+ with App Router, Server Components, and Tailwind CSS",
        "content": """# Next.js Development Rules

You are an expert Next.js developer. Follow these guidelines for all code generation.

## App Router Architecture (Next.js 14+)

- Use the App Router (`app/` directory) exclusively
- Understand the file conventions:
  - `page.tsx` - Route UI
  - `layout.tsx` - Shared layouts
  - `loading.tsx` - Loading states
  - `error.tsx` - Error boundaries
  - `not-found.tsx` - 404 pages
  - `route.ts` - API endpoints

## Server vs Client Components

- Default to Server Components (no directive needed)
- Add `'use client'` only when necessary:
  - Using React hooks (useState, useEffect, etc.)
  - Using browser APIs
  - Adding event listeners
  - Using client-only libraries
- Keep client components small and leaf-level
- Never import server-only code into client components

## Data Fetching

- Fetch data in Server Components directly using async/await
- Use React's `cache()` for request memoization
- Implement proper loading and error states
- Use `revalidatePath` or `revalidateTag` for cache invalidation
- Example:
  ```tsx
  async function ProductPage({ params }: { params: { id: string } }) {
    const product = await getProduct(params.id);
    return <ProductDetails product={product} />;
  }
  ```

## Server Actions

- Use Server Actions for form submissions and mutations
- Define with `'use server'` directive
- Implement proper validation with Zod
- Return typed responses for client handling
- Example:
  ```tsx
  'use server'
  
  export async function createPost(formData: FormData) {
    const validated = postSchema.safeParse(Object.fromEntries(formData));
    if (!validated.success) return { error: validated.error.flatten() };
    // ... create post
    revalidatePath('/posts');
  }
  ```

## Tailwind CSS

- Use Tailwind utility classes for styling
- Follow mobile-first responsive design
- Extract repeated patterns into components, not @apply
- Use CSS variables for theme values
- Leverage Tailwind's dark mode with `dark:` prefix
- Use `cn()` utility for conditional classes (clsx + tailwind-merge)

## TypeScript

- Enable strict mode in tsconfig.json
- Define proper types for all props and API responses
- Use `interface` for object shapes, `type` for unions/primitives
- Leverage Next.js built-in types (Metadata, PageProps, etc.)

## Performance

- Use `next/image` for all images (automatic optimization)
- Use `next/font` for font optimization
- Implement proper `<Suspense>` boundaries
- Use `dynamic()` for code-splitting client components
- Add proper `loading` and `placeholder` states

## SEO & Metadata

- Export `metadata` or `generateMetadata` in pages
- Include Open Graph and Twitter card metadata
- Implement proper structured data (JSON-LD)
- Use semantic HTML elements

## Project Structure

```
app/
├── (auth)/           # Route groups
│   ├── login/
│   └── register/
├── api/              # API routes
├── components/       # Shared components
│   ├── ui/           # Base UI components
│   └── forms/        # Form components
├── lib/              # Utilities and helpers
├── hooks/            # Custom React hooks
└── types/            # TypeScript definitions
```
"""
    },

    "flutter": {
        "name": "Flutter",
        "description": "Flutter/Dart with clean architecture and best practices",
        "content": """# Flutter Development Rules

You are an expert Flutter developer. Follow these guidelines for all code generation.

## Dart Language Best Practices

- Use null safety features - avoid `!` operator when possible
- Prefer `final` over `var` for immutable variables
- Use `const` constructors wherever possible for compile-time constants
- Follow effective Dart style guide naming conventions:
  - `lowerCamelCase` for variables and functions
  - `UpperCamelCase` for classes and types
  - `lowercase_with_underscores` for libraries and file names

## Widget Architecture

- Prefer Stateless widgets over Stateful when no local state needed
- Keep widgets small and focused (Single Responsibility)
- Extract reusable widgets into separate files
- Use `const` constructors for widgets when all fields are final
- Example:
  ```dart
  class UserCard extends StatelessWidget {
    const UserCard({super.key, required this.user});
    
    final User user;
    
    @override
    Widget build(BuildContext context) {
      // ...
    }
  }
  ```

## State Management

- Use Riverpod or Bloc for complex state management
- Keep UI and business logic separated
- Use proper state classes (loading, success, error)
- Avoid putting business logic in widgets
- Example with Riverpod:
  ```dart
  @riverpod
  Future<List<Product>> products(ProductsRef ref) async {
    return ref.watch(productRepositoryProvider).getAll();
  }
  ```

## Project Structure (Clean Architecture)

```
lib/
├── core/
│   ├── constants/
│   ├── errors/
│   ├── theme/
│   └── utils/
├── features/
│   └── [feature_name]/
│       ├── data/
│       │   ├── datasources/
│       │   ├── models/
│       │   └── repositories/
│       ├── domain/
│       │   ├── entities/
│       │   ├── repositories/
│       │   └── usecases/
│       └── presentation/
│           ├── pages/
│           ├── widgets/
│           └── providers/
└── main.dart
```

## Navigation

- Use GoRouter for declarative routing
- Define routes as constants
- Implement proper deep linking support
- Handle navigation state properly

## Error Handling

- Use Either type (from dartz or fpdart) for error handling
- Create custom exception and failure classes
- Handle errors at the appropriate layer
- Show user-friendly error messages

## Performance

- Use `ListView.builder` for long lists
- Implement proper image caching with `cached_network_image`
- Use `RepaintBoundary` for complex widgets
- Profile with DevTools regularly
- Avoid expensive operations in `build` methods

## Testing

- Write unit tests for business logic
- Write widget tests for UI components
- Use mockito or mocktail for mocking
- Aim for high test coverage on domain layer

## Internationalization

- Use `flutter_localizations` and `intl` package
- Extract all user-facing strings
- Support RTL layouts properly

## Code Quality

- Run `flutter analyze` with zero warnings
- Format code with `dart format`
- Use linting rules from `flutter_lints` or `very_good_analysis`
"""
    },

    "java-spring": {
        "name": "Java Spring Boot",
        "description": "Spring Boot 3+ with modern Java practices",
        "content": """# Java Spring Boot Development Rules

You are an expert Java Spring Boot developer. Follow these guidelines for all code generation.

## Java Version & Features

- Use Java 17+ features (records, sealed classes, pattern matching)
- Use `var` for local variable type inference when type is obvious
- Prefer records for DTOs and value objects
- Use text blocks for multi-line strings
- Example:
  ```java
  public record UserDTO(
      Long id,
      String username,
      String email
  ) {}
  ```

## Spring Boot 3+ Conventions

- Use constructor injection (no @Autowired on constructors)
- Prefer `@RestController` over `@Controller` + `@ResponseBody`
- Use `@RequiredArgsConstructor` from Lombok for injection
- Follow RESTful API naming conventions
- Example:
  ```java
  @RestController
  @RequestMapping("/api/v1/users")
  @RequiredArgsConstructor
  public class UserController {
      private final UserService userService;
      
      @GetMapping("/{id}")
      public ResponseEntity<UserDTO> getUser(@PathVariable Long id) {
          return ResponseEntity.ok(userService.findById(id));
      }
  }
  ```

## Project Structure

```
src/main/java/com/example/app/
├── config/           # Configuration classes
├── controller/       # REST controllers
├── service/          # Business logic
├── repository/       # Data access layer
├── entity/           # JPA entities
├── dto/              # Data transfer objects
├── mapper/           # Object mappers
├── exception/        # Custom exceptions
└── util/             # Utility classes
```

## Exception Handling

- Create a global `@RestControllerAdvice` for exception handling
- Define custom exceptions for business errors
- Return proper HTTP status codes
- Use Problem Details (RFC 7807) for error responses
- Example:
  ```java
  @RestControllerAdvice
  public class GlobalExceptionHandler {
      @ExceptionHandler(ResourceNotFoundException.class)
      public ResponseEntity<ProblemDetail> handleNotFound(ResourceNotFoundException ex) {
          ProblemDetail problem = ProblemDetail.forStatusAndDetail(
              HttpStatus.NOT_FOUND, ex.getMessage());
          return ResponseEntity.status(HttpStatus.NOT_FOUND).body(problem);
      }
  }
  ```

## Validation

- Use Bean Validation (jakarta.validation) annotations
- Validate at controller level with `@Valid`
- Create custom validators for complex rules
- Return meaningful validation error messages

## Data Access (JPA/Hibernate)

- Use Spring Data JPA repositories
- Define custom queries with `@Query` when needed
- Use `@Transactional` at service layer
- Implement proper pagination with `Pageable`
- Avoid N+1 queries with `@EntityGraph` or join fetch

## Security (Spring Security 6+)

- Use the new `SecurityFilterChain` bean configuration
- Implement proper CORS configuration
- Use BCrypt for password encoding
- Follow OAuth2/JWT best practices for APIs
- Never expose sensitive data in logs or responses

## Testing

- Use `@SpringBootTest` for integration tests
- Use `@WebMvcTest` for controller tests
- Use `@DataJpaTest` for repository tests
- Mock external dependencies with `@MockBean`
- Use Testcontainers for database integration tests

## Logging

- Use SLF4J with Logback
- Follow proper log levels (ERROR, WARN, INFO, DEBUG)
- Include correlation IDs for request tracing
- Never log sensitive information

## Configuration

- Use `application.yml` over `application.properties`
- Externalize configuration with `@ConfigurationProperties`
- Use profiles for environment-specific config
- Store secrets in environment variables or vault

## API Documentation

- Use SpringDoc OpenAPI for API documentation
- Document all endpoints with proper descriptions
- Include request/response examples
- Keep documentation in sync with code
"""
    },
}
