# EnergyTech-Hackathon


## Energy Consumption Management System

The Energy Consumption Management System is a software application that leverages machine learning algorithms to provide households in Azerbaijan with personalized energy, gas, and water consumption insights. The system collects monthly and daily usage data, generates detailed reports, and presents the information in a user-friendly interface that enables individuals to set consumption goals for themselves.

To ensure accurate and efficient collection of usage data, we propose that utility companies in Azerbaijan switch to an automated meter reading system. This will involve installing electronic devices that can collect usage data automatically and transmit it to the utility company. For households with older meter systems that do not support automated reading, we propose the use of a small Arduino device to calculate the counters automatically. This device can be easily installed near the old system and will provide accurate readings to the utility company.

The system incentivizes users to meet their consumption goals by automatically sending notifications via SMS or email to remind them when they are approaching their monthly limits. Additionally, the system includes machine learning capabilities that provide personalized recommendations on how to reduce energy, gas, and water usage based on individual user habits and consumption patterns.

The system can also be integrated with renewable energy sources such as solar panels and wind turbines to further reduce energy costs and dependence on fossil fuels. By incorporating real-time energy generation data from these sources, the system can provide users with more accurate estimates of their energy consumption and enable them to optimize their energy usage accordingly.

## Technology Stack
Frontend: Chartjs, HTML, CSS
Backend: Python, Django, MongoDB
Machine Learning: Python, Scikit-learn
Automated Meter Reading: Arduino


## Installation

First clone repository:
```
git clone https://github.com/kazimovzaman2/EnergyTech-Hackathon
```

After clone the repository to your local machine. Then, install the necessary dependencies by running:
```
pip install -r requirements.txt
```


You can start the development server by running:
```
python manage.py runserver
```

