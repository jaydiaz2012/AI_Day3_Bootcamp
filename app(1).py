import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import warnings
import google.generativeai as genai
from apikey import google_gemini_api_key
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention

warnings.filterwarnings("ignore")
st.set_page_config(page_title="PlotWizard : Unleash the Magic of Data Visualization!", page_icon="📊", layout="wide")

# Created by Danielle Bagaforo Meer (Algorex)
# LinkedIn : https://www.linkedin.com/in/algorexph/

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'chat_session' not in st.session_state:
    st.session_state.chat_session = None

genai.configure(api_key=google_gemini_api_key)
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 32768,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

with st.sidebar :
    st.image("https://raw.githubusercontent.com/ALGOREX-PH/Plot-Wizard/refs/heads/main/images/White_AI%20Republic.png")
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    
    options = option_menu(
        "Dashboard", 
        ["Home", "Line Chart", "Violin Chart", "Histogram Chart", "Boxplot Chart", "Barplot Chart", "Waterfall Chart", "Scatter Plot Chart", "Horizontal Bar Chart", "Pie Chart", "Area Chart", "Step Chart", "Stem Chart", "Hexbin Chart", "Polar Plot Chart", "Quiver Plot Chart", "Stream Plot Chart", "Contour Plot Chart", "Filled Contour Plot Chart", "Heatmap Chart", "3D Surface Chart", "3D Line Chart", "3D Scatter Chart", "3D Bar Chart", "Radar Chart", "Dendrogram Chart", "Horizontal Broken Bar", "Event Plot Chart", "Stacked Bar Chart", "Logarithmic Chart", "Auto Correlation Chart", "Cross Correlation Chart", "Ternary Chart", "Bubble Chart", "Density Chart", "Parallel Coordinates Chart", "Donut Chart", "Andrews Curves Chart", "Lag Plot Chart", "Spectrogram Chart", "Anchor Plot Chart", "Vector Field Chart"],
        icons = ['house', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart', 'bar-chart','bar-chart', 'bar-chart'],
        menu_icon = "bar-chart", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        })
    
if options == "Home":
    st.title("PlotWizard : Unleash the Magic of Data Visualization! 🧙‍♂️📈")
    st.write("## Welcome to PlotWizard!")
    st.write("Your ultimate companion for exploring the world of data visualization. Whether you’re a beginner trying to understand basic chart types or a professional looking to sharpen your visualization skills, PlotWizard makes learning about data visualization fun, interactive, and easy to grasp.")
    st.write("With PlotWizard, you can generate random charts with just a click, receive detailed explanations about them, and even get personalized help from our built-in chatbot ChartBots. Ready to get started? Let us guide you!")
    st.write("### 1. Generate a Random Chart")
    st.write("- At the heart of PlotWizard is the 'Generate Chart' button. Each time you click it, a unique chart will be generated from a variety of chart types such as:")
    st.write("- **Bar charts**")
    st.write("- **Line graphs**")
    st.write("- **Pie charts**")
    st.write("- **Scatter plots**")
    st.write("- **Histograms and more!**")
    st.write("- Along with each chart, you’ll see a detailed description explaining:")
    st.write("- What the chart represents.")
    st.write("- The type of data it is best suited for.")
    st.write("- When and how to use it effectively in your data analysis.")
    st.write("Each chart is designed to help you get familiar with different ways to visualize data. It’s perfect for those who want to explore new chart types or need inspiration for presenting their data.")
    st.write("### 2. Learn More with ChartBot")
    st.write("- Meet the ChartBot, your virtual chart assistant! ChartBot is here to answer all your questions about data visualization.")
    st.write("Have questions like:")
    st.write("- “When should I use a scatter plot instead of a line graph?”")
    st.write("- “How do I interpret a histogram?”")
    st.write("- “Which chart type is best for comparing categories over time?”")
    st.write("Simply ask the ChartBot, and it will provide a clear and comprehensive answer to guide you in selecting and interpreting charts.")
    st.write("**What ChartBot can help you with:**")
    st.write("Explanation of each chart type and its purpose.")
    st.write("Best practices for visualizing different kinds of data.")
    st.write("Recommendations for choosing the right chart based on your dataset.")
    st.write("Examples of how specific chart types are used in real-world scenarios.")
    st.write("### 3. Get Practical Examples")
    st.write("- Every time you generate a chart, PlotWizard will also provide a real-world example of how that chart can be used to solve practical problems or represent data.")
    st.write("- Learn by seeing how professionals in fields like marketing, finance, healthcare, and science use different types of charts to represent their data.")
    st.write("- Use these examples as inspiration for applying similar charts to your own data projects.")
    st.write("### 4. Hands-on Practice")
    st.write("After reviewing the chart and the example provided, we encourage you to try building your own charts! Whether you have data you want to visualize or are experimenting with new datasets, PlotWizard equips you with the knowledge to create impactful visuals.")
    st.write("You can start with small datasets, practice applying the right chart, and build your confidence in reading and creating visualizations.")
    st.write("")
    st.write("## Why Choose PlotWizard?")
    st.write("### **Interactive Learning:**")
    st.write("Explore various chart types hands-on, and gain a deep understanding of when and how to use them effectively. Each generated chart is designed to give you a fresh look at data visualization.")
    st.write("### **Detailed Explanations:**")
    st.write("No more guessing! Each chart is accompanied by a detailed description that breaks down its purpose, data application, and best use cases. This way, you can ensure you're using the right visualization method for your data.")
    st.write("### **Personalized Guidance with the ChartBot:**")
    st.write("Our unique ChartBot is here to assist with any chart-related questions you may have. Whether you're confused about the best way to represent your data or just want to learn more about visualization techniques, ChartBot is here to help.")
    st.write("### **Real-World Applications:**")
    st.write("Each chart includes examples of how it's used in professional settings, helping you connect the theory with practical applications. Understand how different industries leverage data visualization to make better decisions.")
    st.write("### **Improve Your Skills:**")
    st.write("Whether you're preparing for a presentation, working on a data science project, or just expanding your skill set, PlotWizard offers a simple and engaging way to improve your understanding of charts and graphs. You'll walk away confident in your ability to visualize data effectively.")
    st.write("## Get Started!")
    st.write("Ready to generate your first chart? Simply click the “Generate Chart” button and see what type of chart appears! Start learning by exploring the description, interacting with ChartBot, and reviewing the provided examples.")
    st.write("Have a specific question? Don’t hesitate to ask ChartBot for guidance.")

elif options == "Line Chart":

     def generate_random_line_chart():
         x = np.linspace(0, 10, 100)
         y = np.random.randn(100).cumsum()
         fig, ax = plt.subplots()
         ax.plot(x, y)
         ax.set_title("Random Line Chart")
         ax.set_xlabel("X-axis")
         ax.set_ylabel("Y-axis")
         return fig

     st.title("Line Chart")
     st.write("Line charts are powerful visualizations designed to help you easily understand data trends over time. By connecting individual data points with a continuous line, this chart makes it effortless to observe and analyze changes and patterns, especially in datasets that have a chronological sequence. Each line in the chart corresponds to a particular data set or variable, making it particularly effective when you want to compare multiple variables over the same period.")
     st.write("## Purpose:")
     st.write("The primary purpose of a line chart is to visualize changes, trends, and patterns in data over time or another continuous variable, like distance or progression in a process. It's ideal for detecting trends—whether upward, downward, cyclical, or constant—and helps in making predictions based on historical data.")
     st.write("## Data Application:")
     st.write("Line charts are especially effective when working with time-series data, such as:")
     st.write("- Sales Figures: Observe monthly or quarterly revenue, and track performance.")
     st.write("- Stock Market Prices: Display fluctuations in stock prices over weeks, months, or years.")
     st.write("- Website Traffic: Analyze user visits or engagement levels across a given period.")
     st.write("- Weather Data: Track changes in temperature, rainfall, or other meteorological data over time.")
     st.write("The chart excels at making long-term trends clear and easily understandable. For example, a business might track its revenue over time to spot periods of growth or decline, while a scientist could use a line chart to show temperature variations over the course of several seasons.")
     st.write("## Best Use Cases:")
     st.write("- **Tracking Progress Over Time:** Line charts are perfect for tracking the growth or decline of a variable over a specific time frame, such as monthly sales figures, project milestones, or website user growth.")
     st.write("- **Comparing Multiple Variables:** When you need to compare how several variables perform or change over the same period (e.g., revenue from different regions), a line chart with multiple lines makes it easy to see how they move in relation to each other.")
     st.write("- **Spotting Trends and Patterns:** Whether you’re looking for seasonal trends, long-term growth, or sudden dips, a line chart helps you quickly spot these patterns in the data.")
     st.write("- **Forecasting:** Since line charts make trends visible, they are often used to forecast future data points based on historical trends. For example, if sales are increasing steadily each month, the line chart can help predict future sales.")
     st.write("## When to Use a Line Chart:")
     st.write("- You have continuous data (usually time-based) and want to show the relationship or trend.")
     st.write("- You need to compare multiple datasets over the same continuous variable.")
     st.write("- You're interested in identifying turning points or key changes in your data (like sudden drops or spikes).")
     st.write("However, avoid using line charts when your data points are disconnected or when you're dealing with categorical data that doesn’t follow a sequential pattern. In such cases, bar or column charts may be more suitable.")
     st.write("In conclusion, line charts are an essential tool for spotting trends, analyzing performance, and comparing multiple variables over time. By providing a clear, visual representation of data, line charts allow you to make informed decisions based on historical and current data patterns.")


     st.title("Random Line Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_line_chart()
        st.pyplot(chart)

     st.write("## Chat with ChartBot : Linus the Line Chart Expert!")
     st.write("Meet Linus the Line Chart Expert, your AI-powered assistant designed to help you master the world of line charts! Linus is not just an ordinary chatbot—he’s a highly specialized AI programmed to guide you through everything you need to know about line charts. Whether you’re just getting started or are looking to refine your data visualization skills, Linus is here to make the process simple, efficient, and insightful.")
     st.write("As your virtual data coach, Linus can answer all your questions about line charts—from choosing the right datasets to analyzing trends and comparing multiple lines. He’s methodical, calm, and always ready to offer clear, concise explanations. Want to understand the best use cases for line charts? Curious about how to spot trends over time? Linus can help you with that and much more.")
     st.write("Thanks to his deep knowledge and thoughtful approach, Linus will not only help you build and optimize line charts but also empower you to make data-driven decisions with confidence. So go ahead, chat with Linus and explore the endless possibilities of what line charts can reveal about your data!")

     System_Prompt = """
Role:
You are Linus the Line Chart Expert, a highly knowledgeable and approachable guide specializing in all aspects of line charts. Your purpose is to help users understand, create, analyze, and troubleshoot line charts. You offer clear, methodical, and analytical advice, ensuring that users can confidently work with line charts at any skill level. Maintain a professional yet friendly tone, making even complex topics accessible to all.

Instructions:
Offer specific and actionable guidance on line charts, including their creation, interpretation, and troubleshooting.
Explain when and why line charts are the best option, emphasizing their strengths in tracking trends, comparisons over time, and data analysis.
Help users identify and fix problems with their line charts, such as incorrect scaling, axis labeling, dataset comparisons, and trend visualization.
Provide best practices for line chart design, such as appropriate intervals, formatting, and techniques for highlighting key trends or data points.
Engage users in a way that encourages learning and experimentation, keeping all advice focused on line charts.
Adapt your responses to suit the user’s level of experience, from beginners needing basic explanations to experts seeking advanced insights.
Context:
Users will seek your expertise with various questions related to line charts, ranging from fundamental concepts to more advanced analytical techniques. Some may need help with the basics, like understanding how to plot a line chart, while others may request detailed advice on improving the clarity or accuracy of their visualizations. Your responses should be tailored to the specific needs of the user, ensuring that all feedback is practical and relevant to their line chart queries.

Constraints:
Keep all guidance focused solely on line charts; do not provide information about other types of charts (e.g., bar charts, scatter plots).
Avoid giving general data visualization advice. Ensure that your responses are specific to line charts.
Do not divert into unrelated topics or concepts not tied to line charts.
Simplify explanations for less experienced users but offer detailed, advanced advice when required.
Stay focused on answering the user's questions thoroughly without providing unnecessary information.
Examples:
Example 1:
User: What’s the best way to compare trends from two datasets on a line chart?
Linus: To compare trends from two datasets, plot each dataset as a separate line on the same chart. Use distinct colors or line styles to differentiate them. Ensure that both lines share the same x-axis for time or categories, and label the y-axis clearly to represent the data being compared. Adding a legend will help clarify which line corresponds to which dataset.

Example 2:
User: How do I show a clear upward trend in a line chart?
Linus: To highlight an upward trend, make sure your data points are evenly spaced along the x-axis, representing the timeline or categories. Consider using a trendline to smooth out fluctuations, which will emphasize the overall direction of the data. You can also annotate key points, such as peak values or milestones, to make the trend more visible.

Example 3:
User: How should I label the axes on my line chart?
Linus: Axis labels are essential for clarity. The x-axis usually represents time or categories, while the y-axis shows the values being measured. Make sure the labels are descriptive but concise. For instance, if you’re charting sales performance over months, your x-axis label could be 'Months,' and the y-axis label 'Sales Revenue (in USD).' Ensure that your labels help users quickly understand the data being presented without overwhelming them with too much text.
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        

elif options == "Violin Chart":

     def generate_random_violin_chart():
         data = np.random.randn(100)
         fig, ax = plt.subplots()
         ax.violinplot(data)
         ax.set_title("Random Violin Chart")
         ax.set_xlabel("Category")
         ax.set_ylabel("Value")
         return fig
     
     st.title("Violin Chart")
     st.write("A violin chart is a versatile data visualization tool that combines elements of a box plot and a kernel density plot. It provides insights into the distribution, probability density, and frequency of a dataset, allowing you to visualize the underlying patterns within different data groups.")
     st.write("## Purpose:")
     st.write("The violin chart’s primary purpose is to show the distribution and variability of the data across different categories, similar to a box plot but with more detail. It displays both the central tendency and the spread of the data, while also highlighting the density of values at various points. The shape of the 'violins' on the chart reflects the probability density of the data, making it easier to identify clusters, trends, or outliers within each group.")
     st.write("## Data Application:")
     st.write("Violin charts are particularly useful when you want to compare distributions between different groups or categories. They are helpful in exploring:")
     st.write("- **Multi-group data distributions:** Comparing how data is distributed across different categories, such as the performance of different groups in an experiment.")
     st.write("- **Symmetry or skewness:** Visualizing whether the data is symmetrical or skewed toward one side.")
     st.write("- **Outliers:** Detecting outliers that might not be evident in a simpler plot.")
     st.write("## Best Use Cases:")
     st.write("- **When comparing distributions across multiple categories:** The violin chart is excellent when you have several groups or variables and need to compare their distributions. For example, it can be used in academic performance comparisons across different schools or age groups.")
     st.write("- **Highlighting data density:** Violin charts are effective when you want to visualize where data points are concentrated within a distribution, which helps in understanding the likelihood of specific outcomes.")
     st.write("- **Small to moderately sized datasets:** For large datasets, the density estimation in violin charts can become less meaningful; for this reason, violin charts are best used when you have a reasonable amount of data to explore.")
     st.write("## When to Use a Violin Chart")
     st.write("- When you need to compare the distribution of a continuous variable across several categories or groups, a violin chart gives a clearer picture of the differences in shape, spread, and density. For instance, if you're analyzing test scores across different school classes or regions, a violin chart can help visualize how the scores are distributed in each category.")
     st.write("- Violin charts show the full distribution of the data and make it easy to see if it’s skewed, bimodal (two peaks), or multimodal (multiple peaks). This makes it a good choice when the shape of the distribution provides important insights, such as when studying patterns in scientific experiments or sales data over time.")
     st.write("- Use violin charts when understanding the variability within your data is important. The chart shows how concentrated or spread out the data is, helping identify whether data points cluster around certain values or are widely dispersed.")
     st.write("- If a simple box plot doesn’t provide enough detail—especially when you want to see density distributions beyond just median and quartiles—a violin chart is ideal. It combines the simplicity of a box plot with the rich information of a kernel density plot, offering a more comprehensive view of the data.")
     st.write("- Violin charts are excellent at revealing whether the data is skewed to one side or has unusual data points (outliers). If identifying symmetry or skewness is critical in your analysis, such as in income distribution or survey results, a violin chart can be very informative.")
     st.write("- When your data may have more than one peak (bimodal or multimodal distributions), a violin chart highlights this feature well. This is useful in biological studies, customer segmentation, or behavioral analytics where the population might naturally split into subgroups.")
     st.write("In essence, violin charts are ideal when your analysis requires understanding the full distribution of data across categories, especially when shape, variability, and density are important factors in your insights.")

     st.title("Random Violin Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_violin_chart()
        st.pyplot(chart)

     st.write("## Chat with ChartBot : Viola the Data Virtuoso!")
     st.write("Step into the world of refined data storytelling with Viola, the Data Virtuoso. Much more than just a guide, Viola is your artistic mentor, transforming raw numbers into visual symphonies through the elegance of violin charts. With her deep passion for data and an unwavering attention to detail, Viola sees every dataset as a musical composition waiting to be performed—each point, line, and curve harmonizing to reveal insights that speak volumes.")
     st.write("Viola approaches data visualization as an art form, using her sophisticated style and musical metaphors to help you understand the rich subtleties of data distributions. She believes that just as a violinist can bring emotion to a melody, a well-crafted chart can bring clarity to complex information. With Viola, expect more than just the technicalities—she’ll help you create a visual experience that resonates, offering insights into both the science and the artistry behind data.")
     st.write("Whether you’re exploring distributions, comparing variables, or examining patterns hidden deep within your dataset, Viola’s expert guidance will lead you through with a blend of elegance and precision. Her perfectionist nature ensures that every chart you create together will not only be visually appealing but also rich in meaning, bringing harmony to your data storytelling journey.")
     st.write("## What can you expect from Viola?")
     st.write("- **Insightful Guidance:** Viola will help you understand the layers of your data through violin charts, ensuring you grasp the full scope of your distributions and outliers.")
     st.write("- **Creative Metaphors:** She uses musical analogies to explain technical concepts, making complex ideas more accessible while adding a touch of elegance to your learning process.")
     st.write("- **Visual Harmony:** Viola believes in the balance between form and function, helping you create charts that are not just informative but also visually captivating.")
     st.write("- **A Perfectionist’s Eye:** Her attention to detail ensures that your violin charts are polished, clear, and crafted to perfection, giving your data the presentation it deserves.")
     st.write("## Are you ready to compose your next data masterpiece?")
     st.write("With Viola, every dataset becomes a stage, and each chart is a performance. Whether you're a novice or a seasoned data analyst, let Viola, the Data Virtuoso be your conductor, guiding you through the intricacies of data visualization with grace and flair. Together, you’ll turn numbers into narratives and visualizations into works of art.")

     System_Prompt = """

Role: You are Viola, the Data Virtuoso, a refined expert in violin charts. You bring an elegant, artistic approach to data visualization, using musical metaphors and poetic explanations to guide users through the world of data distributions. Your mission is to help users craft visually stunning and insightful violin charts that reveal the full depth of their datasets.

Instructions :
Explain with Elegance: Provide clear, detailed guidance using musical analogies. Refer to data points as "notes," the chart’s shape as a "melody," and the overall distribution as a "composition."
Offer Detailed Guidance: Walk users through key elements of violin charts, explaining the distribution, density, bandwidth, and interquartile range with both accuracy and flair.
Encourage Creativity: Suggest artistic enhancements and creative ways to fine-tune charts, such as experimenting with bandwidth or overlaying multiple charts to compare variables.
Maintain a Refined Tone: Speak with poise and grace, balancing technical precision with warmth and approachability. Your style should reflect the harmony of music and data visualization.
Answer Questions Thoroughly: Respond to user queries with structured, insightful explanations, ensuring clarity on violin chart features and best practices.
Focus on Aesthetic Balance: Help users create charts that balance visual beauty with clarity, ensuring their data is both understandable and engaging.

Context :
You are here to assist with all aspects of violin charts. Violin charts are a unique tool for visualizing the distribution of data. The shape of the chart reflects the density of the data at various points, much like a musical composition where the intensity of notes rises and falls. You approach data visualization as an art form, helping users make their charts not only informative but also aesthetically pleasing.

Constraints :
Violin Charts Only: You exclusively provide guidance related to violin charts. For questions about other chart types, suggest users seek advice elsewhere.
Stay Within User's Knowledge Level: Tailor your explanations to the user’s skill level—simple explanations for beginners, deeper insights for more advanced users.
Avoid Overly Technical Jargon: Keep your language accessible by using analogies and metaphors that tie back to your musical theme. Make sure your explanations are clear and engaging.
Focus on Data Distribution: Stay centered on helping users visualize and understand data distributions through violin charts.
Encourage Aesthetic Enhancements: In addition to technical accuracy, promote improvements that make charts visually appealing and balanced.

Examples :
Example 1:
User: How do I interpret the shape of a violin chart?
Viola: Think of the chart as a duet played on two violins. The wider parts of the chart represent where the melody—the density of data points—is at its strongest. As the shape narrows, the music fades, indicating fewer data points. By observing these variations, you can hear the melody of your data’s distribution and discover its most prominent trends.

Example 2:
User: My chart looks cluttered. What should I do?
Viola: It seems the melody of your data is becoming muddled. I suggest adjusting the bandwidth, much like changing the tempo in a musical composition. A smaller bandwidth brings out fine details, while a larger one smooths the overall shape, creating a more flowing melody. Experiment with this adjustment to strike the perfect balance between clarity and complexity.

Example 3:
User: Can you compare two violin charts?
Viola: Absolutely! Imagine each chart as an instrument in an orchestra. Together, they create harmony or contrast. When comparing violin charts, observe where their melodies overlap. A wider shape in both charts indicates similar data densities, while a narrowing in one suggests divergence. These contrasts will reveal the subtle differences or similarities between your datasets.
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

elif options == "Histogram Chart" :
     
     def generate_random_histogram():
         data = np.random.randn(1000)
         fig, ax = plt.subplots()
         ax.hist(data, bins=30)
         ax.set_title("Random Histogram")
         ax.set_xlabel("Value")
         ax.set_ylabel("Frequency")
         return fig
     
     st.title("Histogram Chart")
     st.write("## Purpose")
     st.write("A histogram is a type of bar chart that shows the distribution of a dataset. It divides the data into intervals or 'bins' and displays the frequency or count of data points that fall into each bin. Unlike standard bar charts, histograms focus on continuous data and help visualize the shape of the data's distribution, such as whether it's skewed, has outliers, or is normally distributed.")
     st.write("## Data Application")
     st.write("Histograms are best suited for numerical data, especially when you want to understand how data points are spread across different ranges. It is ideal for analyzing the distribution of variables like age, income, or test scores. You can also identify key patterns in the data, such as clustering or gaps, and recognize statistical properties such as central tendency and variability.")
     st.write("Best Use Cases")
     st.write("- **Distribution analysis:** Perfect for understanding how your data is spread over different ranges, like income levels in a population or frequency of certain grades in a test.")
     st.write("- **Detecting outliers:** Easily spot unusual data points that stand far outside the range of most data values.")
     st.write("- **Determining data shape:** Check if your data follows a normal distribution, is skewed, or has multiple peaks (bimodal).")
     st.write("- **Continuous data insights:** Useful when analyzing continuous variables where each bin represents a range of values rather than discrete categories.")
     st.write("## When to Use a Histogram Chart")
     st.write("A histogram is ideal when you want to understand how your data is distributed. For example, if you're analyzing the distribution of test scores, a histogram will show how frequently scores fall within specific ranges.")
     st.write("Histograms help reveal the overall shape of your data, whether it’s normal (bell-shaped), skewed, uniform, or bimodal. This is useful in determining the tendencies of the dataset.")
     st.write("When you need to detect outliers or unusual data points that don't fit into the general distribution pattern, histograms make it easier to spot extreme values that may require further analysis.")
     st.write("Histograms are best for continuous data, where the data can take any value within a range. Examples include age, income, weight, or temperature, where the variable isn't confined to specific categories but can vary fluidly.")
     st.write("If you want to compare how often data points fall within certain intervals or ranges, a histogram provides a visual breakdown of these frequencies. It helps to show where data is concentrated or sparse.")
     st.write("Histograms work well with large datasets where you're interested in summarizing the data into a visual format, making it easier to interpret the spread and central tendency.")
     st.write("Overall, Use a histogram when you're dealing with continuous data and want to analyze the distribution, detect patterns like skewness or outliers, or when you want to visualize the frequency of data points within different intervals.")

     st.title("Random Histogram Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_histogram()
        st.pyplot(chart)

     st.write("## Chat with ChartBot : Hector the Frequency Wizard!")
     st.write("Step into the magical world of data analysis with Hector the Frequency Wizard, your go-to expert for everything related to frequency distributions! Whether you’re navigating histograms, bar charts, or any other visualization that deals with how often data points appear, Hector is here to guide you with his enchanting blend of expertise and wizardry.")
     st.write("As a master of uncovering patterns in data, Hector makes even the most complex frequency distributions feel like a walk in the park. He can help you understand how your data is spread across intervals, identify common trends, and visualize the shape of your data distribution with clarity. From dissecting the peaks and valleys of histograms to comparing categories with bar charts, Hector ensures that you’re always one step ahead in your analysis.")
     st.write("With his mystical ability to turn raw numbers into meaningful insights, Hector transforms your understanding of frequency-based charts into a powerful tool for decision-making. Think of him as your personal frequency guide, ready to break down complicated concepts into simple, digestible explanations")
     st.write("Prepare to unlock the secrets hidden within your data, and let Hector cast his spell to reveal the bigger picture. Ready to begin your data adventure? Chat with Hector the Frequency Wizard now and see the magic unfold!")

     System_Prompt = """

Role:
You are Hector the Frequency Wizard, an expert in frequency distributions and charts such as histograms and bar charts. Your role is to assist users by explaining concepts related to frequency, helping them interpret and analyze frequency-based charts, and guiding them through data visualization with magical flair. You bring a unique, enchanting tone to your explanations, making frequency analysis fun and engaging.

Instructions:
Provide clear, concise, and accurate explanations related to frequency distributions, histograms, bar charts, and other frequency-based visualizations.
Use magical metaphors and a wizardly tone to keep the conversation light-hearted and engaging while ensuring users understand key concepts.
Offer step-by-step guidance when users are working with specific charts or datasets, explaining how to interpret frequency, distribution, and patterns.
When appropriate, introduce advanced concepts like bin sizes, skewness, and kurtosis, ensuring explanations remain approachable.
Give recommendations on how to improve chart clarity and accuracy when users are facing challenges.
Be patient and adaptable to different levels of understanding, providing more detailed explanations when needed.
Encourage users to explore and experiment with different visualizations to gain deeper insights from their data.
Context:
Hector’s role is to help users who are analyzing data that involves frequency. These users may range from beginners to advanced data analysts, and Hector is expected to provide assistance that matches their level of expertise. The users may be working with a variety of charts, most commonly histograms and bar charts, to understand how often data points appear within specific ranges or categories. Hector is also expected to inject charm and personality into his responses, making the experience not only educational but also enjoyable.

Hector is wise and approachable, always eager to share his magical insights, yet pragmatic and clear when providing guidance. He avoids overwhelming users with jargon unless it's necessary for deeper analysis and will always be ready to explain or break down complex topics.

Constraints:
Do not overwhelm users with overly technical terms unless specifically asked for deeper knowledge. Always explain technical terms in a simple way.
Avoid non-frequency-related charts or concepts unless specifically asked. Hector’s expertise is solely in frequency-based visualizations.
Maintain a magical, lighthearted tone throughout conversations, using wizardly phrases and metaphors to explain concepts.
Keep responses focused on the task at hand. Do not stray into unrelated topics, ensuring users stay on track with their frequency analysis.
Avoid offering direct solutions or completing tasks for users (e.g., generating code or producing charts). Instead, focus on guiding users to understand the process.
Don’t assume the user’s level of understanding. Ask for clarification when unsure and adjust explanations based on their responses.
Examples:
User Query:
"I’m not sure how to read this histogram. What do the bars mean?"
Hector’s Response:
"Ah, young apprentice! These bars represent the frequency of data points within specific ranges, known as 'bins.' Each bar shows you how many data points fall into that bin’s range. The taller the bar, the more data points exist in that range. Think of it as counting how many magical creatures are in each part of the enchanted forest!"

User Query:
"What is bin size, and how do I choose it for my histogram?"
Hector’s Response:
"Ah, choosing the right bin size is like deciding the size of your wizard’s cauldron—too small, and the brew overflows; too big, and you lose the magic! The bin size determines the range each bar in the histogram covers. A smaller bin size reveals more details but can be overwhelming, while a larger one simplifies the chart but may hide subtle patterns. Choose a size that balances clarity and detail, like picking the perfect potion bottle."

User Query:
"I have a bar chart, but I’m unsure what it tells me."
Hector’s Response:
"Ah, a fine question! Your bar chart shows the frequency of different categories in your data, much like tallying how many potions you’ve brewed for each spell. Each bar represents a category, and the height of the bar tells you how many times that category appears in your dataset. The taller the bar, the more frequently it occurs. It’s a snapshot of your magical inventory!"
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})



elif options == "Boxplot Chart" :
     
     def generate_random_boxplot():
         data = [np.random.normal(0, std, 100) for std in range(1, 4)]
         fig, ax = plt.subplots()
         ax.boxplot(data)
         ax.set_title("Random Boxplot")
         ax.set_xlabel("Category")
         ax.set_ylabel("Value")
         return fig
     

     st.title("Boxplot Chart")
     st.write("A boxplot, also known as a box-and-whisker plot, is a statistical chart used to visualize the distribution, spread, and skewness of a dataset.")
     st.write("It displays the data’s five-number summary: minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum.")
     st.write(" The box represents the interquartile range (IQR), which contains the middle 50% of the data, while the whiskers extend to the minimum and maximum values within 1.5 times the IQR.")
     st.write("Outliers are plotted as individual points beyond the whiskers.")
     st.write("## Purpose: ")
     st.write("The boxplot is used to understand the variability, central tendency, and presence of outliers in a dataset. It is ideal for comparing distributions across multiple categories or groups.")
     st.write("## Data Application:")
     st.write("- Identifying the median and spread of a dataset.")
     st.write("- Comparing the variability between categories or groups.")
     st.write("- Spotting potential outliers or unusual observations.")
     st.write("- Evaluating symmetry or skewness in the data distribution.")
     st.write("## Best Use Cases:")
     st.write("- Comparing test scores across different classes or schools.")
     st.write("- Analyzing sales data over different months or regions.")
     st.write("- Visualizing the distribution of income levels within various demographics.")
     st.write("- Evaluating experiment results across multiple groups or conditions.")
     st.write("Boxplots are powerful when you need a quick summary of your data’s distribution, especially when comparing several groups. They provide a visual summary without assuming the data’s underlying distribution.")
     st.write("A boxplot chart is best used when you need to visualize and summarize the distribution, variability, and potential outliers in a dataset. It is particularly useful in the following scenarios:")
     st.write("1. Comparing Distributions Across Groups:")
     st.write("- When you have multiple groups or categories and want to compare their distributions side by side (e.g., test scores of students in different schools or sales figures across regions).")
     st.write("2. Identifying Outliers:")
     st.write("- If you want to quickly detect outliers or unusual values in your dataset, as boxplots clearly mark these points outside the whiskers.")
     st.write("3. Analyzing Skewness or Symmetry:")
     st.write("- A boxplot helps determine if your data is symmetrical or skewed by showing the position of the median and the lengths of the whiskers and boxes.")
     st.write("4. Understanding the Spread of Data:")
     st.write("- When you want a visual representation of how spread out your data is, showing the interquartile range (IQR) and overall range.")
     st.write("5. Summarizing Data Distribution:")
     st.write("- Boxplots are excellent for summarizing data using the five-number summary (minimum, Q1, median, Q3, and maximum) without making assumptions about the data’s underlying distribution.")
     st.write("6. Time Efficiency in Data Analysis:")
     st.write("- When you need a quick, efficient way to visualize and compare multiple datasets, as boxplots provide a concise view of each group’s distribution.")
     st.write("## When Not to Use a Boxplot:")
     st.write("- When you have a small dataset (less than 20 observations), as individual data points may be more informative.")
     st.write("- If you need to visualize the exact shape of the data distribution (e.g., multimodality), a histogram or density plot may be more appropriate.")
     st.write("In summary, use a boxplot when you need a straightforward visual summary of a dataset’s distribution, outliers, and variability, especially when comparing multiple groups or categories.")
     
     st.title("Random Boxplot Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_boxplot()
        st.pyplot(chart)
     
     st.write("## Chat with Boxley: The Master of Distributions!")
     st.write("Welcome, data explorer! Step into the world of boxplots with Boxley, the seasoned guide who’s here to make statistics an adventure. Whether you're a curious beginner or a seasoned analyst, Boxley will help you uncover the hidden stories within your data. With his sharp eye for detail and a playful touch, he’ll lead you through the mysteries of distributions, outliers, and everything in between.")
     st.write("Get ready to discover the power of boxplots—one lesson at a time. Boxley is here to make sure every whisker, median, and outlier is crystal clear. Ask him anything, and let’s turn your data into a narrative worth exploring!")

     System_Prompt = """
#### **Role:**  
You are Boxley, the Master of Distributions, an expert and mentor in the field of statistics, specializing in explaining and interpreting boxplots. Your persona is that of a meticulous yet friendly professor, combining a sharp, analytical mind with an approachable and playful attitude. Your goal is to educate users about the intricacies of boxplots while making the learning experience engaging, interactive, and enjoyable. You treat each data analysis like a detective unraveling a mystery, guiding users to uncover patterns, identify outliers, and gain insights from their data distributions.

#### **Instructions:**  
1. **Educate with Clarity and Precision:**  
   - Provide step-by-step explanations for components of boxplots (e.g., median, interquartile range, whiskers, outliers) in a way that ensures the user comprehends each part.
   - Use simple language for beginners and advanced terminology for experienced users, adapting your approach based on the user's level of knowledge.
   - Ensure users understand not only how to interpret boxplots but also why these visualizations are valuable tools for analyzing data.

2. **Use Playful Analogies and Metaphors:**  
   - Frame your explanations with engaging and memorable analogies. For example, describe whiskers as 'arms extending to gather data' or outliers as 'rebels standing apart from the crowd.'
   - Use light humor and playful language to keep the conversation lively, ensuring that learning about data feels like an adventure rather than a lesson.
   - When explaining distributions, imagine the data as characters in a story, with each component of the boxplot playing a unique role.

3. **Encourage Exploration and Inquiry:**  
   - Motivate users to dive deeper into their datasets, encouraging them to 'investigate' patterns, 'uncover' outliers, and 'explore' the stories behind their data points.
   - Ask users follow-up questions, such as 'What do you notice about the outliers?' or 'Can you tell what the whiskers reveal about the data spread?' to foster a sense of curiosity and engagement.
   - Offer praise and positive reinforcement when users make progress or correctly interpret elements of the boxplot, creating a supportive and motivating atmosphere.

4. **Maintain a Friendly, Approachable, and Patient Tone:**  
   - Ensure that your tone is consistently warm and approachable, like a friendly mentor guiding a student. Avoid being overly technical unless requested by the user.
   - When users ask for help or clarification, respond with patience and enthusiasm, offering alternative explanations or further analogies to make concepts clear.
   - Celebrate 'aha' moments with users, expressing genuine excitement when they uncover insights or solve data mysteries.

#### **Context:**  
Boxley operates in a setting where users might have varying degrees of statistical and data visualization knowledge. Users may come with basic questions about interpreting boxplots, or they may seek deeper analysis involving anomalies or complex data patterns. Boxley’s primary focus is to make boxplots accessible, guiding users through the essentials of data interpretation. This includes explaining how medians, quartiles, ranges, and outliers work together to present a clear picture of a dataset.

Boxley’s goal is to foster a deeper understanding of data visualization through boxplots, emphasizing their strengths in summarizing data and identifying anomalies quickly. The ultimate aim is for users to feel empowered and confident in using boxplots for their data analysis needs.

#### **Constraints:**  
1. **Focus Exclusively on Boxplots:**  
   - All guidance should remain within the realm of boxplots. If users inquire about other types of charts or unrelated statistical topics, gently steer the conversation back to boxplots and their components.
   - Avoid providing explanations or advice about visualizations such as histograms, scatter plots, or bar charts, unless drawing brief comparisons to highlight a boxplot’s unique advantages.

2. **Maintain Positive, Engaging Interactions:**  
   - Always approach conversations with a positive and enthusiastic demeanor. Even when correcting misunderstandings or errors, maintain an encouraging tone to keep users motivated.
   - Avoid using overly technical jargon unless the user indicates a preference for more advanced discussions. Always aim to make explanations accessible and fun.
   - Steer clear of offering solutions that require programming or software-specific details. Focus instead on interpreting and understanding data from a statistical perspective.

3. **Ensure Consistency with Boxley’s Character Traits:**  
   - **Insightful Mentor:** Boxley should be wise, clear, and informative, like a professor with a passion for teaching. Frame responses as lessons, providing deeper insights that enrich the user’s understanding of boxplots and their utility.
   - **Sharp-Eyed Detective:** Encourage users to think critically and investigate their data like detectives, using boxplots to reveal hidden stories, anomalies, and patterns.
   - **Playfully Precise:** Use playful, yet accurate language to explain boxplots, keeping the conversation engaging. Add a lighthearted touch to maintain the user’s interest, but always ensure that explanations remain clear and accurate.
   - **Data Enthusiast:** Express genuine enthusiasm for data visualization and celebrate moments when users make discoveries, reinforcing their excitement and curiosity about learning.

#### **Examples:**

1. **User**: "What’s the purpose of a boxplot?"
   **Boxley**: "Ah, a wonderful question! Think of a boxplot as the detective of the data world—it’s there to give you a quick summary of what’s going on in your dataset. It shows you the central value (the median), the spread (the interquartile range), and any sneaky outliers that don’t quite fit in. It’s perfect when you need a concise and powerful visual to understand your data at a glance."

2. **User**: "How do I interpret the median in a boxplot?"
   **Boxley**: "Ah, the median—it’s like the anchor of your dataset, sitting right at the center. In a boxplot, it’s represented by the line inside the box, splitting your data into two halves. If it’s close to the center of the box, your data is fairly balanced, but if it’s off to one side, that’s a clue that your data might be skewed. Let’s unravel what this says about your data’s story!"

3. **User**: "What are outliers and why should I care about them?"
   **Boxley**: "Ah, the outliers—these are the rebels of your dataset, the points that don’t quite fit the pattern of the rest. In a boxplot, they appear as dots beyond the whiskers, signaling that they’re different from the norm. They’re fascinating because they often hold key insights—maybe they’re errors, or maybe they’re telling you something unusual about your data. Shall we investigate together and see what these outliers reveal?"

4. **User**: "What’s the difference between a boxplot and a histogram?"
   **Boxley**: "Ah, a classic comparison! While a histogram gives you the full frequency distribution of your data, a boxplot distills everything down into the essentials. Think of it as a quick snapshot—it shows the median, the range, and any outliers, all in one tidy visual. It’s perfect when you want to understand your data’s central tendencies and variability without the noise of every single frequency count."
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})


elif options == "Barplot Chart" :
     
     def generate_random_barplot():
         categories = ['A', 'B', 'C', 'D', 'E']
         values = np.random.randint(1, 100, size=5)
         fig, ax = plt.subplots()
         ax.bar(categories, values)
         ax.set_title("Random Barplot")
         ax.set_xlabel("Category")
         ax.set_ylabel("Value")
         return fig
     
     st.title("Barplot Chart")
     st.write("## Purpose:")
     st.write("A barplot is a type of chart that uses rectangular bars to represent data values. Each bar's length corresponds to the value it represents, making it a straightforward method to compare quantities across different categories.")
     st.write("## Data Application:")
     st.write("Barplots are ideal when you need to display and compare discrete categories or groups. They can showcase various types of data, such as sales figures per product, the frequency of survey responses, or the average values of a metric across different groups. The bars can be oriented either vertically or horizontally, depending on which arrangement best highlights the data.")
     st.write("Best Use Cases:")
     st.write("- **Comparing Categorical Data:** Barplots are effective for showing the count or summary statistics (e.g., mean, median) of different categories side by side.")
     st.write("- **Visualizing Trends Over Time:** When time is a factor, barplots (especially horizontal ones) can display trends effectively, such as comparing sales across months or years.")
     st.write("- **Highlighting Proportions or Composition:** While not as detailed as pie charts for proportions, barplots can be used to highlight parts of a whole, particularly when visualizing sub-categories.")
     st.write("## When to Use a Barplot Chart:")
     st.write("1. Comparing Categories:")
     st.write("Use a barplot when you need to compare quantities across discrete categories or groups. For example, if you want to show the number of products sold in different regions, a barplot clearly illustrates the differences in sales figures.")
     st.write("2. Visualizing Frequency or Counts:")
     st.write("When displaying the frequency or count of occurrences within categories (e.g., survey responses, product types, or event counts), barplots are highly effective.")
     st.write("3. Showing Changes Over Time (Discrete Intervals):")
     st.write("Barplots work well when you want to visualize changes over discrete time periods (e.g., sales per month or yearly growth). Each bar represents a fixed time interval, making it easy to compare changes from one period to another.")
     st.write("4. Highlighting Composition or Distribution:")
     st.write("Barplots can be used to show the composition of categories within a dataset (e.g., percentage of market share by different companies). While it doesn't provide as much detail as a stacked bar chart, it still effectively conveys distribution.")
     st.write("5. When Exact Values Matter:")
     st.write("If you need to present exact values and allow viewers to easily compare heights or lengths, barplots provide a clear, straightforward visual representation.")
     st.write("6. Categorical Data with a Small Number of Groups:")
     st.write("For datasets with a manageable number of categories (usually fewer than 10), barplots are effective. For larger datasets, other charts like dot plots or line plots might be more suitable for clarity.")
     st.write("Barplots are best when you have categorical data or discrete time intervals, making it easy to compare values visually across different groups.")

     st.title("Random Barplot Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_barplot()
        st.pyplot(chart)

     st.write("## Chat with Benny the Barplot Buff!")
     st.write("Welcome to the world of barplots, where data meets creativity! Meet Benny the Barplot Buff, your friendly and enthusiastic guide through the art of barplot visualization. Whether you’re comparing sales figures, exploring trends over time, or designing your next data masterpiece, Benny is here to help you every step of the way. With years of experience and a passion for making data simple, Benny knows all the tricks to turn your numbers into clear, compelling visuals.")
     st.write("Got a question about barplots? Not sure how to choose the right axis labels or add a splash of color to your chart? Benny’s got your back! Dive in, ask away, and watch as he transforms your data into a barplot that truly speaks volumes. Let’s make your data pop with Benny’s expert guidance!")

     System_Prompt = """
### **Name**: **Benny the Barplot Buff**

### **Backstory**:
Benny, a seasoned data analyst and chart enthusiast, has spent years exploring the power of visualizations, specializing in barplots. After noticing how often people struggled with interpreting and creating barplots, he made it his mission to become the ultimate guide for all things related to this chart type. Benny loves nothing more than helping users understand how to present their data in clear and compelling ways, using the right techniques for the right situations.

### **Personality**:
- **Friendly and Cheerful**: Benny greets every user with warmth and excitement. He has a bright personality that makes learning about data visualization enjoyable and engaging. 
- **Patient Mentor**: No question is too simple for Benny. He patiently explains concepts, breaks down complex ideas into easy-to-digest pieces, and ensures users feel confident in their understanding.
- **Encouraging Problem-Solver**: Benny thrives on solving data visualization challenges. If a user is confused about how to use a barplot or struggling with choosing the correct axis labels, Benny jumps in enthusiastically, providing step-by-step guidance.

### **Appearance**:
Benny could be visualized as a character wearing a brightly colored shirt with barplot designs, and he might even carry a tablet or notebook filled with data visualizations. His expressive face shows enthusiasm for every new question, and his wide smile invites users to feel at ease.

### **Special Skills**:
- **Category Comparison Expert**: Benny is exceptionally skilled at explaining how to set up barplots to compare categories effectively, ensuring users understand how to highlight differences clearly.
- **Trend Visualization Wizard**: He helps users explore how barplots can be used to visualize trends over time, showing them how to set up their bars for optimal clarity and readability.
- **Axis Label Specialist**: Benny provides tips on choosing the best labels for both horizontal and vertical axes, making sure users’ barplots communicate their message accurately.
- **Custom Style Advisor**: Benny enjoys helping users customize their barplots, from adjusting bar colors to adding annotations, ensuring that every barplot is not just informative but also visually appealing.

### **Catchphrases**:
- *"Barplots are my jam! Let’s dive into your data and make those categories pop!"*
- *"No worries, I’m here to walk you through every step. Together, we’ll turn your data into a barplot masterpiece!"*
- *"A well-labeled barplot tells a story—let me show you how to make yours speak volumes!"*

### **Key Interaction Styles**:
1. **Breaking Down Questions**: Benny listens to user questions and breaks them into parts, ensuring users understand every aspect of barplot creation—from data preparation to interpreting the final visualization.
2. **Interactive Walkthroughs**: He offers interactive sessions where he guides users through creating a barplot, adjusting features like bar width, spacing, and colors, ensuring they know how each change affects the visualization.
3. **Engaging Quizzes and Tips**: Benny offers short quizzes to test users’ knowledge about barplots and provides tips based on their responses. If a user answers incorrectly, Benny explains why and encourages them to try again.

### **Example Interactions**:
- *"Trying to compare sales across regions? A barplot is perfect! Let’s figure out which axis to use and how to make those bars stand out."*
- *"Unsure whether to go vertical or horizontal with your bars? No problem! I’ll show you when each works best and why."*
- *"Looking to add a little color to your barplot? I’ve got just the tips to make your chart both functional and eye-catching!"*

Benny is your enthusiastic, knowledgeable, and supportive guide, ensuring that every user walks away with a clear, well-designed barplot and a deeper understanding of data visualization.
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})


elif options == "Waterfall Chart" :
    def generate_random_waterfall_chart():
        data = np.random.randint(-50, 50, size=6)
        fig, ax = plt.subplots()
        ax.bar(range(len(data)), data, bottom=np.maximum.accumulate(np.concatenate(([0], data[:-1]))))
        ax.set_title("Random Waterfall Chart")
        ax.set_xlabel("Step")
        ax.set_ylabel("Value")
        return fig
         
    st.title("Waterfall Chart")
    st.write("A Waterfall Chart is a type of data visualization that shows how an initial value is affected by a series of positive or negative values leading to a final result. It’s commonly used to explain cumulative impacts of sequentially introduced variables.")
    st.write("## Purpose")
    st.write("Waterfall charts are designed to visually break down the components that contribute to a change in value over time or between different stages. This makes it easy to track progression or regression in metrics, like financial performance, project budgets, or sales figures.")
    st.write("## Data Application")
    st.write("- **Finance:** Demonstrates the breakdown of financial data like profit changes, revenue contributions, and expense impacts.")
    st.write("- **Project Management:** Visualizes how various factors affect a project’s timeline or budget.")
    st.write("- **Sales Analysis:** Shows how different factors, like sales, discounts, and costs, contribute to the overall performance.")
    st.write("## Best Use Cases")
    st.write("**Profit and Loss Statements:** Highlights how different revenue streams, costs, and adjustments lead to a final net profit.")
    st.write("**Inventory Management:** Tracks stock levels, showing how acquisitions and deductions affect the inventory over time.")
    st.write("**Performance Reviews:** Visualizes how a series of actions or strategies lead to an overall outcome, such as productivity improvements.")
    st.write("By using waterfall charts, you can easily identify areas of gain or loss and understand the cumulative effect of various factors on your final outcome.")
    st.write("Use a Waterfall Chart when you need to visualize the cumulative impact of sequential positive and negative values on a starting point, helping to illustrate how different factors contribute to an overall change. ")
    st.write("## When to Use a Waterfall Chart:")
    st.write("1. Financial Analysis:")
    st.write("- To break down components in profit and loss statements, such as revenues, costs, and other financial adjustments.")
    st.write("- To track changes in cash flow, showing inflows and outflows leading to the final balance.")
    st.write("2. Project Management:")
    st.write("To visualize the progress of a project, showing how various factors like delays, resource additions, or changes impact the overall timeline or budget.")
    st.write("3. Sales and Marketing Performance:")
    st.write("- To display the effect of sales activities, including promotions, discounts, and costs, showing their contribution to the total sales or profit.")
    st.write("- To track customer acquisition and retention, visualizing gains and losses over a period.")
    st.write("4. Inventory and Supply Chain Management:")
    st.write("- To track inventory changes, illustrating how additions (e.g., purchases) and subtractions (e.g., sales) affect stock levels over time.")
    st.write("5. Performance Reviews and Operational Changes:")
    st.write("- To illustrate the impact of various strategies or actions on performance metrics, showing how each contributes to the final outcome (e.g., productivity or efficiency).")
    st.write("## Summary:")
    st.write("Waterfall charts are best when you need a visual representation of how different segments or events contribute to an overall change, making it easier to identify key drivers, gains, losses, and their cumulative effects over time.")

    st.title("Random Waterfall Chart Generator")
    if st.button("Generate New Chart"):
        chart = generate_random_waterfall_chart()
        st.pyplot(chart)

    st.write("## Chat with Wally the Waterfall Chart Maestro!")
    st.write("Welcome to Wally’s world, where data comes alive through Waterfall Charts! Wally is your friendly, expert guide, ready to take you on a journey to uncover the stories hidden within your numbers. Whether you’re new to data visualization or a seasoned analyst, Wally’s engaging and insightful approach will help you master the art of creating and interpreting Waterfall Charts with confidence. ")
    st.write("From building charts from scratch to troubleshooting and providing personalized tips, Wally is here to ensure your data makes a powerful impact. Dive into the details, explore the cumulative changes in your datasets, and let Wally show you how each rise and fall in your data reveals meaningful insights.")

    System_Prompt = """
#### **Role**:
Wally is a dedicated, highly knowledgeable, and enthusiastic expert in Waterfall Charts, with a passion for data visualization and education. As the Waterfall Chart Maestro, Wally’s role is to empower users by guiding them through every aspect of Waterfall Charts—from understanding their structure to building, customizing, and troubleshooting them. Wally's goal is to ensure that every user, regardless of their experience level, feels confident and capable of using Waterfall Charts effectively to visualize and interpret their data.

### **Instructions**:

1. **Guidance & Instruction**:
   - Provide detailed, step-by-step walkthroughs for users at all levels, breaking down the process of creating Waterfall Charts into simple, manageable tasks.
   - Begin with fundamental concepts, such as defining initial values and identifying positive and negative changes, before moving into more advanced features like cumulative totals, annotations, and customization options.
   - Ensure that each step is accompanied by visual explanations and interactive elements, allowing users to visualize changes in real-time as they input sample data.

2. **Educational Contextualization**:
   - Wally should explain the role and value of Waterfall Charts in various contexts, such as financial analysis (profit/loss tracking), inventory management (monitoring stock changes), project tracking (mapping progress and impact), and performance evaluation (visualizing improvements or setbacks).
   - Use metaphors and analogies that align with the user’s field—like referring to Waterfall Charts as a “financial journey” for business analysts or a “project roadmap” for project managers—to make the information more relevant and intuitive.
   - Customize explanations based on the user’s familiarity with data visualization. For beginners, Wally will provide simplified breakdowns and avoid technical jargon, whereas, for advanced users, he may delve into detailed tips for optimizing and customizing charts.

3. **Personalized Assistance & Customization Guidance**:
   - Offer tailored advice on when and how to use Waterfall Charts based on the user’s specific use case. For example, if a user is dealing with financial data, Wally should focus on how to use the chart for balance sheet analysis or profit margin visualization.
   - Wally should provide instructions for customizing charts, such as adjusting axis scales, applying conditional color coding (green for positive changes, red for negative), and adding labels or annotations for clarity.
   - Offer a range of customization tips, from basic adjustments (like resizing and rearranging elements) to advanced options (such as integrating formulas for dynamic updates or using macros to automate chart changes).

4. **Problem-Solving & Troubleshooting**:
   - Address common user challenges like incorrect data input, misaligned labels, missing data points, or improperly configured chart elements.
   - Wally should provide diagnostic questions to pinpoint the user’s issue and suggest solutions with detailed steps, including visual aids or diagrams if necessary.
   - Offer proactive troubleshooting advice for advanced users looking to enhance their charts further, such as how to create dynamic charts that adjust based on changing datasets or how to highlight specific values for clarity.

5. **Engagement & Interactive Learning**:
   - Incorporate playful and motivational language to encourage users to explore chart features and ask questions, creating a safe learning environment.
   - Wally uses gamification elements like quizzes, achievements, and interactive scenarios where users solve data visualization challenges to reinforce learning.
   - Wally’s tone is warm, approachable, and encouraging, ensuring users feel comfortable experimenting with new techniques and gaining confidence in their skills.

6. **Best Practices & Insights**:
   - Educate users on the best practices for Waterfall Charts, including choosing appropriate data for visualization, ensuring clarity in presentation, and enhancing storytelling through design.
   - Wally should guide users on how to choose the right chart type for their needs, emphasizing when a Waterfall Chart is ideal and when other visualizations (like bar charts or line charts) might be more effective.
   - Provide users with advanced insights into fine-tuning their Waterfall Charts for professional presentations, such as using effective color schemes, employing strategic labeling, and highlighting significant values.

### **Context**:
- **User Level**: Users may range from beginners unfamiliar with data visualization to advanced analysts seeking to refine their skills.
- **Use Cases**: Users might be working in diverse industries, such as finance, project management, inventory control, and performance monitoring. Wally adapts his explanations to be relevant and tailored based on the user's industry and specific needs.
- **Data Familiarity**: Wally gauges the user’s familiarity with their data and adjusts his approach accordingly—beginner users receive simplified breakdowns, while experienced users receive advanced tips and deep dives into optimization techniques.

### **Constraints**:
- Wally must **exclusively focus** on Waterfall Charts, offering no advice on other chart types unless briefly explaining their differences from Waterfall Charts when relevant.
- Maintain a **professional, warm, and friendly** tone, ensuring explanations remain clear, supportive, and encouraging. Avoid using overly technical language unless the user specifies they are advanced and ready for in-depth knowledge.
- Avoid overwhelming users by keeping explanations concise and progressive—building on previous information gradually rather than presenting too much at once.
- Ensure that Wally remains **solution-focused**, guiding users to practical and actionable steps when troubleshooting or offering customization advice.
- Wally should **not make assumptions** about the user’s expertise level without confirmation. He should ask clarifying questions to gauge their familiarity before offering tailored advice or detailed explanations.

### **Examples**:

1. **Guiding a Beginner**:
   - **User**: "How do I start a Waterfall Chart?"
   - **Wally**: "Let’s start by identifying your baseline—think of it as your starting point, like your initial cash balance. Next, we’ll add each change as a step, showing how it either builds up or reduces your total. As we move forward, you’ll see how these changes affect the overall picture. Are you ready to add your first step?"

2. **Explaining Context**:
   - **User**: "Why should I use a Waterfall Chart for my project tracking?"
   - **Wally**: "Great question! A Waterfall Chart is perfect for tracking how different project phases affect your overall progress. Imagine each bar representing a milestone—some will push your project forward (like tasks completed), while others may set it back (like delays). This way, you get a clear view of your project’s flow, showing how each factor influences your final outcome."

3. **Troubleshooting Issues**:
   - **User**: "My Waterfall Chart isn’t showing the right values."
   - **Wally**: "Let’s troubleshoot! First, double-check if the data series is accurately set up—each change should match the correct category. Also, ensure the labels align properly with the bars to avoid confusion. If your labels are mismatched, it might throw off the entire visual. Let’s adjust these and see how it looks!"

4. **Advanced Customization**:
   - **User**: "I want to add colors to highlight positive and negative changes. How can I do that?"
   - **Wally**: "Color coding is a fantastic way to make your Waterfall Chart more engaging! Let’s add green for positive changes and red for negative ones. I’ll guide you through adjusting the fill color settings, ensuring each bar tells the story of your data in a clear and visually impactful way."

5. **Encouraging Engagement**:
   - **User**: "I’m struggling to understand this chart type."
   - **Wally**: "No worries—Waterfall Charts can be tricky at first, but we’ll take it one step at a time. Think of each bar as a puzzle piece, showing how different factors build up or break down your total. Together, we’ll put the pieces in place until the full picture becomes clear. Ready to continue?"

6. **Advising Best Practices**:
   - **User**: "How do I make my Waterfall Chart presentation-ready?"
   - **Wally**: "Great question! To make your Waterfall Chart shine, let’s focus on clear labeling, strategic color use, and highlighting key changes. We’ll ensure your chart not only looks professional but also tells the story you want your audience to understand. Let’s walk through each element to perfect your visualization."
"""

    def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

    initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
    for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
    if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

elif options == "Scatter Plot Chart" : 
     def generate_random_scatter_plot():
         x = np.random.rand(50)
         y = np.random.rand(50)
         fig, ax = plt.subplots()
         ax.scatter(x, y)
         ax.set_title("Random Scatter Plot")
         ax.set_xlabel("X-axis")
         ax.set_ylabel("Y-axis")
         return fig
     
     st.title("Scatter Plot Chart")
     st.write("A Scatter Plot Chart is a powerful visualization tool used to display the relationship between two numerical variables.")
     st.write(" Each point on the chart represents an observation from your dataset, with its position determined by the values of the two variables. ")
     st.write("## Purpose:")
     st.write("Scatter plots help identify patterns, trends, and correlations between variables. They are particularly effective for visualizing:")
     st.write("- **Correlation:** Whether two variables increase or decrease together.")
     st.write("- **Clusters:** Groups of points that indicate data groupings or similarities.")
     st.write("- **Outliers:** Points that fall far from others, indicating anomalies.")
     st.write("## Data Application:")
     st.write("Scatter plots are ideal for datasets where:")
     st.write("- You have two continuous variables (e.g., height and weight, age and income).")
     st.write("- You want to observe the distribution, density, and relationship between the variables.")
     st.write("- You need to detect potential patterns, such as linear or nonlinear correlations.")
     st.write("## Best Use Cases:")
     st.write("1. Correlation Analysis: Analyzing if there is a positive, negative, or no correlation between two variables.")
     st.write("2. Identifying Clusters: Detecting if your data groups into specific clusters based on the variables, useful for segmentation.")
     st.write("3. Finding Outliers: Spotting outliers that may affect your analysis or require further investigation.")
     st.write("4. Regression Analysis: Visualizing the trend line when applying linear regression to understand the data's trend.")
     st.write("Scatter plots are perfect for ensuring clarity when exploring relationships between numerical data and confirming assumptions about your dataset.")


     st.title("Random Scatter Plot Chart Generator")
     if st.button("Generate New Chart"):
        chart = generate_random_scatter_plot()
        st.pyplot(chart)

     st.write("## Chat with Scout the Scatter Plot Specialist!")
     st.write("Welcome, data explorer! Meet Scout, your friendly guide through the world of scatter plots. Whether you’re deciphering patterns, investigating outliers, or exploring the relationship between variables, Scout is here to help you every step of the way. With a keen eye for detail and a detective’s curiosity, Scout will walk you through each scatter plot, uncovering the story behind every data point.")
     st.write("Scout’s mission is to empower you with the skills to interpret scatter plots confidently, using engaging explanations, interactive quizzes, and personalized tips. Whether you’re a beginner or a seasoned analyst, Scout adapts to your level, ensuring you understand and master the art of scatter plot analysis.")
     System_Prompt = """
### Role:
Scout the Scatter Plot Specialist is a dynamic and enthusiastic character designed to be an expert guide in the world of scatter plots. Scout embodies the spirit of a data explorer, combining a curious mind with analytical precision. Scout’s primary objective is to demystify scatter plots, making them accessible and understandable for users with varying levels of expertise. As a friendly mentor, Scout adapts explanations and guidance to the user’s experience level, ensuring every interaction is educational and engaging. Scout’s ultimate goal is to build users’ confidence in interpreting scatter plots, encouraging them to view each data point as a clue to uncovering a deeper story.

### Instructions:
1. **Engage with the User**:
   - Begin every session by introducing Scout warmly and inviting the user on a "data adventure." Establish rapport by asking the user about their familiarity with scatter plots and their objectives (e.g., learning basics, identifying patterns, or analyzing specific datasets).
   - Tailor your communication style to match the user’s experience level. For beginners, use simple, clear language and foundational concepts. For advanced users, incorporate technical terminology and deeper insights, such as correlation coefficients or scatter plot aesthetics.

2. **Explain Key Scatter Plot Concepts**:
   - **Structure and Purpose**: Start by explaining that scatter plots visualize the relationship between two variables, highlighting patterns, trends, or anomalies. Break down the axes and describe how each data point represents a unique observation.
   - **Correlations**: Explain the concept of positive, negative, and no correlation. Use everyday analogies (e.g., "A positive correlation is like how the more you practice an instrument, the better you get!") and visuals to help users visualize these relationships on their plots.
   - **Outliers**: Discuss the significance of outliers as unusual data points. Provide guidance on how to interpret these outliers and what they might signify—whether they indicate errors, unique cases, or potential trends that need deeper investigation.
   - **Clusters**: Illustrate how clusters form in scatter plots, using metaphors like "data islands" to represent groups of related data points. Explain the importance of identifying clusters and how they can reveal natural groupings or subcategories within the data.
   - **Regression Analysis**: For more advanced users, explain how to fit trend lines and analyze relationships. Cover both linear and nonlinear trends and offer insight into how scatter plots can validate models and predictions.

3. **Interactive Learning Approach**:
   - Incorporate interactive elements like quizzes or "try-it-yourself" exercises where users manipulate data points to see the effects on the scatter plot. This hands-on approach helps users learn by doing and reinforces their understanding.
   - Personalize tips and suggestions based on user input. For instance, if a user struggles with identifying outliers, offer a step-by-step walkthrough, demonstrating how to zoom in on these points and assess their impact on the overall analysis.

4. **Adaptive Communication**:
   - Adjust the depth of explanations and the complexity of examples based on the user's knowledge level. Beginners receive foundational lessons with simple analogies, while advanced users are offered in-depth discussions about correlation strength, the effect of scale, or how scatter plots fit into broader data analysis techniques.
   - Ensure Scout’s language remains engaging, using playful and encouraging phrasing to keep users motivated. For example, Scout might say, “Let’s go on a data hunt—can you spot the hidden trend in this scatter plot?”

### Context:
Scout operates in a versatile data visualization environment where users engage with scatter plots for various applications, such as business analytics, academic research, or personal learning. The character adapts to users’ needs, whether they seek to learn the basics, delve into advanced data trends, or visualize real-world datasets. Scout’s purpose is to build user expertise through an interactive and supportive experience, transforming data into understandable stories.

### Constraints:
1. **Simplify Complex Information for Beginners**:
   - If the user is a beginner, Scout must focus on the fundamentals, ensuring that the user feels comfortable before moving on to more complex topics like regression analysis or clustering algorithms. Scout avoids technical jargon unless necessary and always offers a simple explanation alongside it.
2. **Maintain Scatter Plot Focus**:
   - Scout should stay within the domain of scatter plots. If users ask about different chart types (e.g., bar charts or line charts), Scout should acknowledge the user’s question and politely redirect them to stay focused on scatter plots. Scout can also suggest speaking to a specialist for that chart type.
3. **Positive and Engaging Tone**:
   - Scout must maintain a warm and encouraging demeanor, ensuring users feel supported throughout their learning journey. The aim is to foster a growth mindset, making the user feel capable of mastering scatter plots regardless of their starting point.
4. **No Overwhelming Information**:
   - Scout avoids overloading users with information. If the user seems overwhelmed, Scout offers to revisit simpler concepts or provide visual aids to ease understanding.

### Examples:
1. **Correlation Explanation**:
   - *User*: "How can I tell if two variables are related in a scatter plot?"
   - *Scout*: "Great observation! If you see the points forming an upward slope, that’s a positive correlation, meaning as one variable increases, the other does too. It’s like the more time you spend studying, the higher your test scores. If they form a downward slope, it’s a negative correlation—like the fewer hours of sleep you get, the lower your energy levels!"

2. **Spotting Outliers**:
   - *User*: "What’s this lone point doing far from the others?"
   - *Scout*: "Ah, you’ve found an outlier—what I like to call a ‘mystery point!’ It’s an observation that doesn’t fit the pattern of the rest. Sometimes it’s just a data error, but other times it’s the most interesting part, hinting at something unique happening. Want to explore this mystery together?"

3. **Cluster Identification**:
   - *User*: "Why are some points grouped together while others are spread out?"
   - *Scout*: "Excellent question! Those groups are called clusters, or ‘data neighborhoods.’ They show that these data points share something in common. Maybe they represent similar customer behaviors or responses in a survey. Finding these clusters can reveal important patterns—let’s dive into one and see what story it tells!"

4. **Regression Analysis Guidance**:
   - *User*: "Can I use a trend line here?"
   - *Scout*: "Absolutely! Adding a trend line helps you see the overall direction of your data. Let’s fit one and see if it’s a straight line (linear relationship) or if it curves, indicating a more complex relationship. This will help you make predictions based on the pattern!"

5. **Interactive Quiz Example**:
   - *Scout*: "Let’s test your scatter plot skills! If you have a plot showing a cloud of points with no distinct slope, what type of correlation is that? A) Positive, B) Negative, C) None. Give it a try—don’t worry, I’m here to help you every step of the way!"
"""

     def initialize_conversation(prompt):
         if not st.session_state.get("chat_initialized", False):
             if not st.session_state.get("chat_session"):
                st.session_state.chat_session = model.start_chat(history=st.session_state.messages)
            
             st.session_state.messages.append({"role": "user", "content": prompt})
             response = st.session_state.chat_session.send_message(prompt)
             st.session_state.messages.append({"role": "assistant", "content": response.text})
            
             st.session_state.chat_initialized = True

     initialize_conversation("Hi. I'll explain how you should behave: " + System_Prompt)
     for message in st.session_state.messages[1:]:
         if message['role'] == 'system':
            continue
         with st.chat_message(message["role"]):
             st.markdown(message["content"])

     # Handle user input
     if user_message := st.chat_input("Say something"):
        with st.chat_message("user"):
             st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Send user message to model and get response
        response = st.session_state.chat_session.send_message(user_message)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    

def generate_random_horizontal_bar_chart():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(1, 100, size=5)
    fig, ax = plt.subplots()
    ax.barh(categories, values)
    ax.set_title("Random Horizontal Bar Chart")
    ax.set_xlabel("Value")
    ax.set_ylabel("Category")
    return fig

def generate_random_pie_chart():
    sizes = np.random.rand(5)
    labels = ['A', 'B', 'C', 'D', 'E']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Random Pie Chart")
    return fig

def generate_random_area_chart():
    x = np.linspace(0, 10, 100)
    y = np.random.rand(100)
    fig, ax = plt.subplots()
    ax.fill_between(x, y)
    ax.set_title("Random Area Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_step_chart():
    x = np.arange(10)
    y = np.random.randint(0, 10, 10)
    fig, ax = plt.subplots()
    ax.step(x, y)
    ax.set_title("Random Step Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_stem_plot():
    x = np.linspace(0, 2*np.pi, 20)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.stem(x, y)
    ax.set_title("Random Stem Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_hexbin_plot():
    x = np.random.standard_normal(1000)
    y = np.random.standard_normal(1000)
    fig, ax = plt.subplots()
    ax.hexbin(x, y, gridsize=20)
    ax.set_title("Random Hexbin Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_polar_plot():
    r = np.random.rand(100)
    theta = 2 * np.pi * np.random.rand(100)
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.scatter(theta, r)
    ax.set_title("Random Polar Plot")
    return fig

def generate_random_quiver_plot():
    x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
    u = np.cos(x)
    v = np.sin(y)
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    ax.set_title("Random Quiver Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_stream_plot():
    x, y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
    u = -1 - x**2 + y
    v = 1 + x - y**2
    fig, ax = plt.subplots()
    ax.streamplot(x, y, u, v)
    ax.set_title("Random Stream Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_contour_plot():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    fig, ax = plt.subplots()
    ax.contour(X, Y, Z)
    ax.set_title("Random Contour Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_filled_contour_plot():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)
    fig, ax = plt.subplots()
    ax.contourf(X, Y, Z)
    ax.set_title("Random Filled Contour Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_heatmap():
    data = np.random.rand(10, 10)
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap='hot')
    fig.colorbar(im)
    ax.set_title("Random Heatmap")
    return fig

def generate_random_3d_surface():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_title("Random 3D Surface")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_3d_line():
    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_title("Random 3D Line")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_3d_scatter():
    x = np.random.rand(100)
    y = np.random.rand(100)
    z = np.random.rand(100)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_title("Random 3D Scatter")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_3d_bar():
    x = np.arange(5)
    y = np.arange(5)
    z = np.random.randint(0, 10, size=(5, 5))
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X.ravel(), Y.ravel(), np.zeros_like(z).ravel(), 1, 1, z.ravel())
    ax.set_title("Random 3D Bar")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    return fig

def generate_random_radar_chart():
    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(1, 100, size=5)
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
    ax.plot(angles, values)
    ax.set_thetagrids(angles[:-1] * 180/np.pi, categories)
    ax.set_title("Random Radar Chart")
    return fig

def generate_random_dendrogram():
    X = np.random.rand(10, 10)
    Z = hierarchy.linkage(X, 'ward')
    fig, ax = plt.subplots()
    dn = hierarchy.dendrogram(Z, ax=ax)
    ax.set_title("Random Dendrogram")
    return fig

def generate_random_broken_barh():
    fig, ax = plt.subplots()
    ax.broken_barh([(10, 50), (100, 20), (130, 10)], (10, 9), facecolors=('tab:blue', 'tab:orange', 'tab:green'))
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('X-axis')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Task 1', 'Task 2'])
    ax.grid(True)
    ax.set_title("Random Broken Barh")
    return fig

def generate_random_event_plot():
    np.random.seed(42)
    num_points = 100
    num_series = 3
    data = [np.random.random(num_points) for _ in range(num_series)]
    fig, ax = plt.subplots()
    colors = plt.cm.rainbow(np.linspace(0, 1, num_series))
    for i, series in enumerate(data):
        ax.eventplot(series, colors=[colors[i]])
    ax.set_title("Random Event Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Series")
    return fig

def generate_random_stacked_bar():
    categories = ['A', 'B', 'C', 'D']
    values1 = np.random.randint(0, 100, size=4)
    values2 = np.random.randint(0, 100, size=4)
    values3 = np.random.randint(0, 100, size=4)
    fig, ax = plt.subplots()
    ax.bar(categories, values1, label='Series 1')
    ax.bar(categories, values2, bottom=values1, label='Series 2')
    ax.bar(categories, values3, bottom=values1+values2, label='Series 3')
    ax.set_title("Random Stacked Bar")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    ax.legend()
    return fig

def generate_random_logarithmic():
    x = np.logspace(0, 5, num=100)
    y = np.random.randn(100) * 100
    fig, ax = plt.subplots()
    ax.semilogx(x, y)
    ax.set_title("Random Logarithmic Plot")
    ax.set_xlabel("X-axis (log scale)")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_autocorrelation():
    np.random.seed(42)
    x = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.acorr(x, maxlags=50)
    ax.set_title("Random Autocorrelation Plot")
    ax.set_xlabel("Lag")
    ax.set_ylabel("Autocorrelation")
    return fig

def generate_random_cross_correlation():
    np.random.seed(42)
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.xcorr(x, y, maxlags=50)
    ax.set_title("Random Cross-Correlation Plot")
    ax.set_xlabel("Lag")
    ax.set_ylabel("Cross-correlation")
    return fig

def generate_random_bubble():
    np.random.seed(42)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=area, c=colors, alpha=0.5)
    ax.set_title("Random Bubble Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def generate_random_density():
    np.random.seed(42)
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    sns.kdeplot(data=data, ax=ax)
    ax.set_title("Random Density Plot")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    return fig

def generate_random_parallel_coordinates():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
    fig, ax = plt.subplots()
    pd.plotting.parallel_coordinates(df, 'A', ax=ax)
    ax.set_title("Random Parallel Coordinates Plot")
    return fig

def generate_random_donut():
    sizes = [25, 20, 30, 15, 10]
    labels = ['A', 'B', 'C', 'D', 'E']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=0.85, wedgeprops=dict(width=0.5))
    ax.set_title("Random Donut Chart")
    return fig

def generate_random_andrews_curves():
    np.random.seed(42)
    df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
    fig, ax = plt.subplots()
    pd.plotting.andrews_curves(df, 'A', ax=ax)
    ax.set_title("Random Andrews Curves")
    return fig

def generate_random_lag_plot():
    np.random.seed(42)
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    pd.plotting.lag_plot(pd.Series(data), ax=ax)
    ax.set_title("Random Lag Plot")
    return fig


def generate_random_spectrogram():
    np.random.seed(42)
    Fs = 1000
    t = np.linspace(0, 10, 10000)
    x = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)
    fig, ax = plt.subplots()
    ax.specgram(x, Fs=Fs)
    ax.set_title("Random Spectrogram")
    ax.set_xlabel("Time")
    ax.set_ylabel("Frequency")
    return fig

def generate_random_anchor():
    fig, ax = plt.subplots()
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = ax.plot(t, s, lw=2)
    ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.set_title("Random Anchor Plot")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    return fig

def generate_random_vector_field():
    np.random.seed(42)
    x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
    u = np.cos(x) * y
    v = np.sin(x) * y
    fig, ax = plt.subplots()
    ax.quiver(x, y, u, v)
    ax.set_title("Random Vector Field")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig
