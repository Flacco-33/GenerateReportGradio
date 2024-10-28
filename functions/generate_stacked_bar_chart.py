import matplotlib.pyplot as plt

def generate_stacked_bar_chart(rating_aspects):
    """
    Generates a stacked bar chart based on the provided rating aspects.
    Args:
        rating_aspects (dict): A dictionary where keys are strings representing aspect numbers 
                               ('1', '2', '3', '4') and values are dictionaries with 'positive' 
                               and 'negative' keys representing the respective values.
    Returns:
        None: The function saves the generated chart as 'temp/image3.png'.
    """
    categories = ['aspecto 1', 'aspecto 2', 'aspecto 3', 'aspecto 4']

    positive_values = [rating_aspects[str(i)]['positive'] for i in range(1, 5)]
    negative_values = [rating_aspects[str(i)]['negative'] for i in range(1, 5)]

    fig, ax = plt.subplots()
    ax.bar(categories, positive_values, color='navy', label='Positivas')
    ax.bar(categories, negative_values, bottom=positive_values, color='sandybrown', label='Negativas')

    ax.set_xlabel('Categorías')
    
    ax.legend()

    # plt.show()

    fig.savefig('temp/image3.png')
