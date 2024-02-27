# CollabChatbot Beta: Elevate Your Employee Information and Team-Building Experience with LLM and your SQL data! 🚀 

![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)






A powerful LLM based Chatbot system developed by [MindInventory](https://mindinventory.com/)

Welcome to CollabChatbot – your personal assistant designed to streamline access to employee data and enhance team-building efforts. This beta version introduces a powerful suite of features that redefine how you interact with employee information and foster collaboration within your organization.

## Key Features:

- **Personal Info:** Obtain instant details on any employee. 🧑‍💼
- **Occupancy:** Access real-time updates on employee locations. 📍
- **Skills:** Effortlessly identify specific skill sets of your team members. 💼🔍
- **Recommendations:** Receive smart team-building suggestions based on skills and occupancy. 🤝



https://github.com/Mindinventory/Collabchatbot-Gemini-LLM/assets/156774622/683c3412-dff8-498c-82ec-0b604b8de70f




### Advanced Technology Integration 🤖

CollabChatbot is built on an innovative integration of cutting-edge tools and frameworks, ensuring unparalleled functionality and efficiency. Developed with a unique blend of technologies, including Pandas, Llamacpp, Gemini Pro, Langchain, and FastAPI, it excels in generating dynamic Pandas queries for seamless tabular data retrieval and manipulation.

This advanced technological foundation guarantees that CollabChatbot provides users with an intuitive and powerful solution for accessing and analyzing employee information. Elevate your workplace experience with CollabChatbot Beta – where efficiency meets collaboration seamlessly. 

# Project Setup 👨‍💻🚀

Welcome to our awesome project! 🎉 Follow these simple steps to get everything up and running smoothly.

### Prerequisites 🛠️

- **Python Version:** This project requires Python ^3.10.12. Make sure you have it installed on your machine.

### Setting up the Environment 🌐

1. **Virtual Environment:**
    
    ```bash
    python -m venv venv
    ```
    
2. **Install Dependencies:**
    
    ```bash
    source venv/bin/activate  # activate virtual environment (Linux/Mac)
    pip install -r requirements.txt
    ```
    
3. **Environment Variables:**
Create a `.env` file in the root directory and add your Google API Key:
    
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```
    

### Repository Configuration 📁

1. **Cache Directory:**
Create a `cache` directory inside `src/repositories`:
    
    ```bash
    mkdir src/repositories/cache
    ```
    
2. **Cache Files:**
Inside the `src/repositories/cache` directory, create the following files:
    - `employee_profile.pkl`
    - `team_info.pkl`
    - `agenda_management.pkl`

### Run the Application 🚀

1. **Change Directory:**
    
    ```bash
    cd src
    ```
    
2. **Run Uvicorn:**
    
    ```bash
    uvicorn main:app --reload
    ```

### Connecting CollabChatbot with SQL Database 🗃️

CollabChatbot is not just about accessing employee information; it goes a step further by seamlessly integrating with SQL databases commonly used in enterprise businesses. This powerful integration allows CollabChatbot to harness the full potential of Large Language Models (LLM) and SQL data, providing a comprehensive solution for organizational needs.

* SQL Database Integration 🔄
CollabChatbot connects effortlessly with your SQL database, enabling real-time access to structured data. By utilizing the power of SQL queries, it facilitates:

* Customized Data Retrieval: Tailor your queries to retrieve specific employee details, team information, or any other relevant data directly from your SQL database.

* Dynamic Data Manipulation: Perform dynamic data manipulations and transformations using SQL queries, ensuring that the information presented is always up-to-date and relevant.

### Enterprise Business Benefits 🏢

1. Data Security and Compliance 🔒
CollabChatbot ensures that sensitive employee information stored in SQL databases remains secure. It adheres to industry standards for data privacy and compliance, providing a reliable and secure platform for accessing essential organizational data.

2. Enhanced Decision-Making 💡
By seamlessly integrating with SQL databases, CollabChatbot empowers decision-makers with real-time, accurate data. This enhances the decision-making process by providing insights into employee skills, team structures, and occupancy, ultimately contributing to more informed and strategic decisions.

3. Streamlined Collaboration 👥
Efficient collaboration is at the heart of CollabChatbot. The integration with SQL databases streamlines access to collaborative tools, ensuring that teams can easily leverage the platform to enhance communication, project planning, and overall team productivity.

4. Scalability and Flexibility 🚀
CollabChatbot's integration with SQL databases ensures scalability and adaptability to the evolving needs of your enterprise. As your organization grows, CollabChatbot grows with it, effortlessly handling increased data volumes and expanding functionalities.

###  SQL Integration Setup 🛠️

1. SQLAlchemy Integration:

* CollabChatbot utilizes SQLAlchemy to establish a connection with your SQL database. Ensure that you have the necessary SQLAlchemy configurations set up in your project.

2. SQL Query Execution:

* Leverage the power of SQL queries to interact with your database. CollabChatbot's advanced technology seamlessly integrates these queries, allowing for dynamic data retrieval and manipulation.

3. Data Mapping:

* Define clear data mappings between your SQL database schema and CollabChatbot's data models. This ensures accurate interpretation and presentation of the retrieved information.
By combining the capabilities of LLM, SQL data, and CollabChatbot's advanced features, your organization can elevate its employee information and team-building experience to new heights. Welcome to a future where technology meets collaboration seamlessly! 🚀🌐

That's it! 🚀 Your project is now up and running. ✨
