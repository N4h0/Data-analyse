import csv
import matplotlib.pyplot as plt
import numpy as np


data = []

with open('responser.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # Append the row to the data list
        data.append(row)

def parse_score(value):
    try:
        return int(value)
    except ValueError:
        if value.strip().lower() == 'ja':
            return 1
        elif value.strip().lower() == 'nei':
            return 0
        return None  # Return None for invalid entries


# Initialize lists to hold scores for each question
mobile_navigation_scores = []
pc_navigation_scores = []
mobile_visual_scores = []
pc_visual_scores = []
mobile_responsiveness_scores = []
pc_responsiveness_scores = []
mobile_layout_scores = []
pc_layout_scores = []
mobile_images_fonts_scores = []
pc_images_fonts_scores = []
mobile_design_improvement_scores = []
pc_design_improvement_scores = []
mobile_interactive_elements_scores = []
pc_interactive_elements_scores = []

def parse_score(value):
    try:
        return int(value)
    except ValueError:
        if value.strip().lower() == 'ja':
            return 1
        elif value.strip().lower() == 'nei':
            return 0
        return None  # Return None for invalid entries

# Iterate through the data to gather scores
for row in data:
    tool_used = row["Hvilket verkøy brukte du for å navigere på nettsiden?"].strip().lower()
    navigation_score = parse_score(row["Hvor enkelt var det å navigere på nettsiden?"])
    visual_score = parse_score(row["Hvor tilfredsstillende var den visuelle utformingen av nettsiden for deg?"])
    responsiveness_score = parse_score(row["Hvor fornøyd er du med nettsidens responsivitet og lastetid?"])
    layout_score = parse_score(row["Hvordan var den generelle opplevelsen av nettsidens layout og organisering av innholdet?"])
    images_fonts_score = parse_score(row["Hvordan vurderer du valg av bilder, fontvalg og tekststørrelser?"])
    design_improvement_score = parse_score(row["Hvor enig er du i at designet forbedret brukeropplevelsen på nettsiden?"])
    interactive_elements_score = parse_score(row["Fungerte alle interaktive elementer og funksjoner som forventet?"])
    
    if tool_used == 'mobil' or tool_used == 'mobile':
        if navigation_score is not None:
            mobile_navigation_scores.append(navigation_score)
        if visual_score is not None:
            mobile_visual_scores.append(visual_score)
        if responsiveness_score is not None:
            mobile_responsiveness_scores.append(responsiveness_score)
        if layout_score is not None:
            mobile_layout_scores.append(layout_score)
        if images_fonts_score is not None:
            mobile_images_fonts_scores.append(images_fonts_score)
        if design_improvement_score is not None:
            mobile_design_improvement_scores.append(design_improvement_score)
        if interactive_elements_score is not None:
            mobile_interactive_elements_scores.append(interactive_elements_score)
    elif tool_used == 'pc':
        if navigation_score is not None:
            pc_navigation_scores.append(navigation_score)
        if visual_score is not None:
            pc_visual_scores.append(visual_score)
        if responsiveness_score is not None:
            pc_responsiveness_scores.append(responsiveness_score)
        if layout_score is not None:
            pc_layout_scores.append(layout_score)
        if images_fonts_score is not None:
            pc_images_fonts_scores.append(images_fonts_score)
        if design_improvement_score is not None:
            pc_design_improvement_scores.append(design_improvement_score)
        if interactive_elements_score is not None:
            pc_interactive_elements_scores.append(interactive_elements_score)

# Calculate average scores and standard deviations
def calculate_avg_and_std(scores):
    avg = np.mean(scores)
    std = np.std(scores)
    return avg, std

avg_mobile_navigation, std_mobile_navigation = calculate_avg_and_std(mobile_navigation_scores)
avg_pc_navigation, std_pc_navigation = calculate_avg_and_std(pc_navigation_scores)
avg_mobile_visual, std_mobile_visual = calculate_avg_and_std(mobile_visual_scores)
avg_pc_visual, std_pc_visual = calculate_avg_and_std(pc_visual_scores)
avg_mobile_responsiveness, std_mobile_responsiveness = calculate_avg_and_std(mobile_responsiveness_scores)
avg_pc_responsiveness, std_pc_responsiveness = calculate_avg_and_std(pc_responsiveness_scores)
avg_mobile_layout, std_mobile_layout = calculate_avg_and_std(mobile_layout_scores)
avg_pc_layout, std_pc_layout = calculate_avg_and_std(pc_layout_scores)
avg_mobile_images_fonts, std_mobile_images_fonts = calculate_avg_and_std(mobile_images_fonts_scores)
avg_pc_images_fonts, std_pc_images_fonts = calculate_avg_and_std(pc_images_fonts_scores)
avg_mobile_design_improvement, std_mobile_design_improvement = calculate_avg_and_std(mobile_design_improvement_scores)
avg_pc_design_improvement, std_pc_design_improvement = calculate_avg_and_std(pc_design_improvement_scores)
avg_mobile_interactive_elements, std_mobile_interactive_elements = calculate_avg_and_std(mobile_interactive_elements_scores)
avg_pc_interactive_elements, std_pc_interactive_elements = calculate_avg_and_std(pc_interactive_elements_scores)

# Create the combined plot
fig, ax = plt.subplots(figsize=(18, 10))

width = 0.35
x_labels = [
    'Enkel navigasjon',
    'Visuell tilfredsstillelse',
    'Responsivitet',
    'Layout og organisering',
    'Bilder, fontvalg og tekststørrelser',
    'Design forbedret brukeropplevelse',
    'Interaktive elementer fungerte'
]
x = np.arange(len(x_labels))

mobile_avgs = [
    avg_mobile_navigation, avg_mobile_visual, avg_mobile_responsiveness,
    avg_mobile_layout, avg_mobile_images_fonts, avg_mobile_design_improvement,
    avg_mobile_interactive_elements
]
pc_avgs = [
    avg_pc_navigation, avg_pc_visual, avg_pc_responsiveness,
    avg_pc_layout, avg_pc_images_fonts, avg_pc_design_improvement,
    avg_pc_interactive_elements
]
mobile_stds = [
    std_mobile_navigation, std_mobile_visual, std_mobile_responsiveness,
    std_mobile_layout, std_mobile_images_fonts, std_mobile_design_improvement,
    std_mobile_interactive_elements
]
pc_stds = [
    std_pc_navigation, std_pc_visual, std_pc_responsiveness,
    std_pc_layout, std_pc_images_fonts, std_pc_design_improvement,
    std_pc_interactive_elements
]

bars1 = ax.bar(x - width/2, mobile_avgs, width, yerr=mobile_stds, label='Mobil', color='blue', capsize=10, alpha=0.7)
bars2 = ax.bar(x + width/2, pc_avgs, width, yerr=pc_stds, label='PC', color='green', capsize=10, alpha=0.7)

# Set titles and labels with larger fonts
ax.set_title('Gjennomsnittlige tilfredsstilhet med feilmargin (stdev)', fontsize=20)
ax.set_ylabel('Gjennomsnittlig score', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(x_labels, rotation=45, ha='right', fontsize=14)
ax.legend(fontsize=14)

# Adding data labels inside the bars with larger font size
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval - 0.2, f'{yval:.2f}', ha='center', va='top', fontsize=12, color='white', fontweight='bold')

# Adjust layout
plt.tight_layout()
plt.show()