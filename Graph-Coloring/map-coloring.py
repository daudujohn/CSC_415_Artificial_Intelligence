import networkx as nx
import matplotlib.pyplot as plt

def backtracking_search(csp: nx.Graph):
    return backtrack(csp, {})

def backtrack(csp: nx.Graph):
    chosen_variable = select_unassigned_variable(csp)
    ordered_domain_values = order_domain_values(csp, chosen_variable)
    for value in ordered_domain_values:
        is_satisfied = satistfies_constraints(csp, chosen_variable, value)
        if is_satisfied:
            csp.nodes[chosen_variable]['color'] = value
        inferences = inference(csp, chosen_variable)

def select_unassigned_variable(csp: nx.Graph):
    degrees = [degree for node, degree in csp.degree]
    highest_degree = max(degrees)
    index_of_highest_degree = degrees.index(highest_degree)
    chosen_node = list(csp.nodes())[index_of_highest_degree]
    return chosen_node

def order_domain_values(csp: nx.Graph, variable): 
    available_choices = csp.nodes[variable]['available_choices']

    impact_dict = {choice: 0 for choice in available_choices}

    for choice in available_choices:
        for adj_node in csp[variable]:
            adjacent_available_choices = list(csp.nodes[adj_node]['available_choices'])
            if choice in adjacent_available_choices:
                adjacent_available_choices_copy = adjacent_available_choices.copy()
                adjacent_available_choices_copy.remove(choice)
                csp.nodes[adj_node]['available_choices'] = adjacent_available_choices_copy

                if len(adjacent_available_choices_copy) == 0:
                    impact_dict[choice] += 2
                else:
                    impact_dict[choice] += 1
            
            csp.nodes[adj_node]['available_choices'] = adjacent_available_choices

    sorted_choices = sorted(available_choices, key=lambda choice: impact_dict[choice])

    return sorted_choices

def satistfies_constraints(csp: nx.Graph, variable, value):
    for node in G[variable]:
        if G.nodes[node]['color']:
            if G.nodes[node]['color'] == value:
                return False
    
    return True

def inference(csp: nx.Graph, variable):
    pass

G = nx.Graph()

default_attributes = {"color": "", "available_choices": ['red', 'green', 'blue']}
G.add_nodes_from([
    ("NT", default_attributes),
    ("WA", {"color": "red", "available_choices": ['red', 'green', 'blue']}),
    ("Q", default_attributes),
    ("SA", default_attributes),
    ("NSW", default_attributes),
    ("V", default_attributes),
    ("T", default_attributes),
])

G.add_edges_from([("SA", "WA"), ("SA", "NT"), 
                  ("SA", "Q"), ("SA", "NSW"), 
                  ("SA", "V"), ("WA", "NT"), 
                  ("NT", "Q"), ("Q", "NSW"), 
                  ("NSW", "V")])

# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='light', )

# plt.show()