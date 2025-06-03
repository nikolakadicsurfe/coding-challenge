## Setup Instructions

1. Install Python 3.8 or higher
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

### Endpoints

1. **Fetch User by ID**
   - **Endpoint:** `/api/user/<int:user_id>/`
   - **Description:** Retrieves user information based on the user ID.

2. **Get Total Actions for User**
   - **Endpoint:** `/api/user/<int:user_id>/actions/`
   - **Description:** Retrieves the total number of actions performed by a user.

3. **Get Action Type Breakdown**
   - **Endpoint:** `/api/actions/<str:action_type>/breakdown/`
   - **Description:** Provides a breakdown of a specific type of action.

4. **Calculate Referral Index**
   - **Endpoint:** `/api/referral-index/`
   - **Description:** Calculates the referral index.
