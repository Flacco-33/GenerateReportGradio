import matplotlib.pyplot as plt

def generate_pie_chart(emotions):
    """
    Generates and displays a pie chart based on the given emotions and their percentages.
    Args:
        emotions (dict): A dictionary where keys are emotion names (str) and values are their corresponding percentages (float).
    Returns:
        None: The function saves the generated chart as 'temp/image2.png'.
    """
    emotions_list = list(emotions.keys())
    percentages = list(emotions.values())
    
    fig, ax = plt.subplots()
    ax.pie(percentages, labels=emotions_list, autopct='%1.1f%%', startangle=90)

    ax.set_title('Distribución de emociones')

    # plt.show()

    fig.savefig('temp/image2.png')
