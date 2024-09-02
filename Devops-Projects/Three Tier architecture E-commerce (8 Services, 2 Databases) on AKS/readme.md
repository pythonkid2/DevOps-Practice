# Three Tier architecture E-commerce (8 Services, 2 Databases) on AKS

- Understand what is three tier architecuture
- How different services connect to each other in three tier architecture
- How to create Dockerfiles for each service ?
- How to create Deployment, Service and Ingress
- How does Ingress controller work ?
- Expose the three tier application to end users.

![Screenshot 2024-02-16 at 1 43 25 PM](https://github.com/iam-veeramalla/Azure-zero-to-hero/assets/43399466/0623a010-d8f1-4632-abce-d06f5755b1fa)

Repo link: https://github.com/pythonkid2/three-tier-architecture-project

### Microservices Architecture for Stance Robot Shop

1. **User Service**  
   - **Functionality:** Handles user registration, validation (e.g., email format, password strength), and login.  
   - **Flow:** The first step is user registration. Validation checks (like email and password policies) ensure valid inputs. Once registered, the user credentials are securely stored in the database. After successful registration, users can log in to the platform.  
   - **Database:** MongoDB, storing user information such as usernames, passwords, and other related data.

2. **Catalog Service**  
   - **Functionality:** Manages product catalogs, including various categories, product descriptions, prices, and images.  
   - **Flow:** After logging in, the user can browse the catalog to explore products. The catalog microservice fetches product details like descriptions, pricing, and images from its database.  
   - **Database:** MySQL, storing product information and associated images.

3. **Cart Service**  
   - **Functionality:** Allows users to add products to their cart and maintains the state of the cart even if the user logs out.  
   - **Flow:** Users can add products (robots) to the cart, and the cart data persists even across sessions (e.g., when logging out and logging back in). Once the user proceeds to checkout and buys the product, the items are removed from the cart. If they don’t complete the payment, the items remain in the cart for later.  
   - **Persistent Cart:** Cart data is maintained until the payment process is completed.

4. **Shipping Service**  
   - **Functionality:** Calculates shipping costs based on the user's location.  
   - **Flow:** After the cart is confirmed, shipping costs are computed based on the product’s destination. This service factors in location and distance to determine shipping fees. In real-world applications, this might involve querying a shipping provider's API or using a predefined formula.

5. **Payment Service**  
   - **Functionality:** Manages the payment process.  
   - **Flow:** After calculating shipping costs, the user is prompted to complete the payment. The payment service handles the transaction and ensures payment is successfully processed before moving to the next step.

6. **Dispatch Service**  
   - **Functionality:** Manages the dispatch process once the payment is completed and provides tracking information.  
   - **Flow:** After successful payment, the dispatch service prepares the product for shipment and provides tracking information to the user, confirming that the product is ready for delivery.

7. **Rating Service**  
   - **Functionality:** Handles product ratings, allowing users to rate and review products dynamically.  
   - **Flow:** After receiving and using the product, users can rate it. Ratings are stored dynamically, and changes reflect immediately. The rating data is stored in an in-memory data store (Redis) for fast retrieval, given the frequent and dynamic nature of the updates.

8. **Web Service**  
   - **Functionality:** Hosts the front-end web interface for the e-commerce platform.  
   - **Flow:** The web service, built with technologies like Angular, React, or simple HTML/CSS/JavaScript, serves as the user interface. This microservice runs on a web server like Nginx or Apache and is responsible for serving the application to users.

### Databases
- **MongoDB:** Used for storing user-related information, such as registration details, usernames, passwords, and other personal data.
- **MySQL:** Used for product-related data, including product descriptions, prices, and images.

### Additional Considerations:
- **Programming Languages:** Each microservice is implemented in different programming languages (e.g., Node.js for Cart, Python for Payments, PHP for Dispatch) to demonstrate the versatility of microservice architecture. In real-world scenarios, however, teams may choose a single language for consistency. This diversity of languages helps DevOps engineers gain experience with writing Dockerfiles for various environments.
  
- **In-Memory Data Store (Redis):** Used in the Rating Service for fast, dynamic updates. Redis is set up as a StatefulSet in Kubernetes with persistent volumes to ensure data persistence in case of failure.

### Deployment Strategy:
- Each microservice is containerized and independently deployable. The goal is to ensure that each service can be updated, scaled, or replaced without affecting the other services, enhancing the flexibility, maintainability, and reliability of the system.


27


