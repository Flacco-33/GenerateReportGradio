import matplotlib.pyplot as plt

def generate_bar_chart(teacherEvaluations):
    """
    Generates a bar chart based on teacher evaluations.
    Parameters:
    teacherEvaluations (dict): A dictionary where keys are strings representing 
                               aspects (e.g., '1', '2', '3', '4') and values are 
                               the corresponding evaluation scores.
    The function creates a bar chart with the following aspects:
    - 'aspecto 1'
    - 'aspecto 2'
    - 'aspecto 3'
    - 'aspecto 4'
    The chart displays the evaluation scores for each aspect. If an aspect is 
    not present in the dictionary, it defaults to a score of 0. The y-axis 
    ranges from 0 to 5. The generated chart is displayed and saved as 
    'temp/image4.png'.
    """
    categories = ['aspecto 1', 'aspecto 2', 'aspecto 3', 'aspecto 4']
    calificaciones = [teacherEvaluations.get(str(i), 0) for i in range(1, 5)]

    fig, ax = plt.subplots()
    ax.bar(categories, calificaciones, color='olivedrab', label='Calificación')

    ax.set_xlabel('Aspectos')
    ax.set_ylabel('Calificación')
    ax.set_ylim(0, 5)

    plt.show()
    fig.savefig('temp/image4.png')