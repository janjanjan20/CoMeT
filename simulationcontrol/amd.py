
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
#test
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


def whole_grid(max_x, max_y, max_z):

    results = np.zeros((max_x, max_y, max_z))

    for i in range(0, max_x):
        for j in range(0, max_y):
            for k in range(0, max_z):
                results[i, j, k] = calc_one(i, j, k, max_x, max_y, max_z)

    print(results)
    return results

def calc_one(x, y, z, max_x, max_y, max_z):

    total = 0

    for i in range(0, max_x):
        for j in range(0, max_y):
            for k in range(0, max_z):

                # if [x, y, z] != [max_x, max_y, max_z]:

                total += abs(i - x) + abs(j - y) + abs(k - z)

    return total / (max_x * max_y * max_z)



    



if __name__ == '__main__':
    
    data = whole_grid(4, 4, 4)

    fig, axs = plt.subplots(4)
    fig.suptitle('Average Manhattan Distance')

    for d in range(0, len(data)):
        # colors_list = ['#cfd4e4', '#9aabe0', '#647ed3', '#3a5fd5']
        colors_list = ['#9af8fd', '#02d6e1', 'blue', 'darkblue'] 
        cmap = colors.ListedColormap(colors_list) 
        
        # Plot the heatmap with custom colors and annotations 
        axs[d].imshow(data[d], cmap=cmap, vmin=3,vmax=4.5, extent=[0, 4, 0, 4]) 
        for i in range(4): 
            for j in range(4):
                if data[d][i][j] == 4.5:
                    axs[d].annotate(str(data[d][i][j]), xy=(j+0.5, i+0.5), 
                                ha='center', va='center', color='white')
                elif int(data[d][i][j]) == data[d][i][j]:
                    axs[d].annotate(str(int(data[d][i][j])), xy=(j+0.5, i+0.5), 
                                ha='center', va='center', color='black')
                else:
                    axs[d].annotate(str(data[d][i][j]), xy=(j+0.5, i+0.5), 
                                ha='center', va='center', color='black')
        
        # Add colorbar 
        # cbar = axs[d]._colorbars(ticks=[3.2, 4.3], fraction=0.046, pad=0.04) 
        # cbar.ax.set_yticklabels(['3', '4.5']) 
        
        # Set plot title and axis labels 
        # axs[d].set_title("Z Coordinate " + str(d)) 
        #axs[d].xlabel("Core X Coordinate")
        axs[d].set_xticks([0.5, 1.5, 2.5, 3.5], [0,1,2,3])
        #axs[d].ylabel("Core Y Coordinate")
        axs[d].set_yticks([0.5, 1.5, 2.5, 3.5], [0,1,2,3])

        # axs[d].set(xlabel='x-label', ylabel='y-label')

        # # Display the plot 
        # plt.show() 

    for ax in axs.flat:
        ax.set(xlabel="X Coordinate", ylabel="Y Coordinate")

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    # plt.show()

    # --------------------------------------------------------------------------------------------------------


    # from mpl_toolkits.mplot3d import Axes3D
    # import numpy as np
    # import matplotlib.pyplot as plt

    # ax = plt.figure().add_subplot(projection='3d')

    # x = np.linspace(0, 3, 4)
    # X, Y = np.meshgrid(x, x)
    # Z =[[ 0.,          0.,         -0.,          0.        ],
    #     [-0.,         -0.01353234,  0.02679383, -0.03951904],
    #     [-0.,         -0.00767723,  0.01520079, -0.02242012],
    #     [ 0.,          0.00917686, -0.01817005,  0.02679956]]
    
    # Z =[[0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0]]

    # print(X)
    # print(Y)
    # print(.1*np.sin(3*X)*np.sin(5*Y))
    # print(data[0])
    # # print(Z)
    # # print(Z.size)
    # # print(Z[0].size)
    # # print(Z[0][0].size)

    # levels = np.linspace(-1, 1, 40)

    # ax.contourf(X, Y, data[0], zdir='z')
    # ax.contourf(X, Y, data[1], zdir='z')
    # # ax.contourf(X, Y, 3+.1*np.sin(5*X)*np.sin(8*Y), zdir='z', levels=3+.1*levels)
    # # ax.contourf(X, Y, 7+.1*np.sin(7*X)*np.sin(3*Y), zdir='z', levels=7+.1*levels)

    # # ax.contourf(X, Y, data[0], zdir='z', levels=.1*levels)
    # # ax.contourf(X, Y, data[1], zdir='z', levels=3+.1*levels)
    # # ax.contourf(X, Y, data[2], zdir='z', levels=7+.1*levels)

    # ax.legend()
    # ax.set_xlim3d(0, 3)
    # ax.set_ylim3d(0, 3)
    # ax.set_zlim3d(0, 10)

    # plt.show()










    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    # Sample data generation
    layers = 4  # Number of layers
    rows = 4    # Number of rows per layer
    cols = 4    # Number of columns per layer

    # data = np.random.rand(layers, rows, cols)

    # Set up the figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Customize the colormap
    cmap = plt.get_cmap('viridis')

    colors_list = ['#cfd4e4', '#9aabe0', '#647ed3', '#3a5fd5'] 
    cmap = colors.ListedColormap(colors_list)

    # Function to create a square at a given position
    def create_square(x, y, z, value):
        square = [
            [x - 0.5, y- 0.5, z],
            [x + 1- 0.5, y- 0.5, z],
            [x + 1- 0.5, y + 1- 0.5, z],
            [x- 0.5, y + 1- 0.5, z]
        ]
        return square
    
    def get_color(value):
        if value == 3:
            return '#cfd4e4'
        elif value == 3.5:
            return '#9aabe0'
        elif value == 4:
            return '#647ed3'
        elif value == 4.5:
            return '#3a5fd5'
        
    # Define the spacing between layers
    layer_spacing = 1

    # Loop through each layer and plot flat squares
    for z in range(layers):
        for y in range(rows):
            for x in range(cols):
                value = data[z, y, x]
                square = create_square(x, y, z * layer_spacing, value)
                color = get_color(value)
                poly = Poly3DCollection([square], color=color, alpha=0.75)
                ax.add_collection3d(poly)
                ax.text(x, y, z * layer_spacing + 0.3, f'{value:.2f}', color='black', ha='center', va='center')

    # Set labels
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Layer')

    # Set title
    ax.set_title('3D Layered Heatmap with Flat Squares')


    # Set axis ticks and labels
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels([0, 1, 2, 3])
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels([0, 1, 2, 3])
    ax.set_zticks([0, 1, 2, 3])
    ax.set_zticklabels([0, 1, 2, 3])

    # Set axis limits
    ax.set_xlim(0- 0.5, cols - 0.5)
    ax.set_ylim(0- 0.5, rows - 0.5)
    ax.set_zlim(0, layers * layer_spacing - 1)

    # Show plot
    # plt.show()






    #--------------------------------------------------------------------------------------------------------
    # Sample data generation
    layers = 4  # Number of layers
    rows = 4    # Number of rows per layer
    cols = 4    # Number of columns per layer

    # data = np.random.rand(layers, rows, cols)

    # Set up the figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Customize the colormap
    # cmap = plt.get_cmap('viridis')

    # colors_list = ['#cfd4e4', '#9aabe0', '#647ed3', '#3a5fd5'] 
    colors_list = ['#9af8fd', '#02d6e1', 'blue', 'darkblue'] 
    cmap = colors.ListedColormap(colors_list)

    # Function to create a square at a given position
    def create_square(x, y, z, value):
        square = [
            [x - 0.5, y- 0.5, z],
            [x + 1- 0.5, y- 0.5, z],
            [x + 1- 0.5, y + 1- 0.5, z],
            [x- 0.5, y + 1- 0.5, z]
        ]
        return square
    
    def get_color(value):
        if value == 3:
            return colors_list[0]
        elif value == 3.5:
            return colors_list[1]
        elif value == 4:
            return colors_list[2]
        elif value == 4.5:
            return colors_list[3]
        
    # Define the spacing between layers
    layer_spacing = 1

    # Loop through each layer and plot flat squares
    for z in range(layers):
        for y in range(rows):
            for x in range(cols):
                value = data[z, y, x]
                square = create_square(x, y, z * layer_spacing, value)
                color = get_color(value)
                poly = Poly3DCollection([square], color=color, alpha=0.75)
                ax.add_collection3d(poly)
                # ax.text(x, y, z * layer_spacing + 0.3, f'{value:.2f}', color='black', ha='center', va='center')

    # Set labels
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    ax.set_zlabel('Z coordinate')

    # Set title
    # ax.set_title('Average Manhattan Distance of cores in 4x4x4 network')


    # Customize the colorbar
    norm = plt.Normalize(data.min() -0.25, data.max() +0.25)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    fig.colorbar(sm, label='Average Manhattan Distance', ticks=[3, 3.5, 4, 4.5])

    # Hide grid lines
    ax.grid(False)
    
    # Set axis ticks and labels
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels([0, 1, 2, 3])
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels([0, 1, 2, 3])
    ax.set_zticks([0, 1, 2, 3])
    ax.set_zticklabels([0, 1, 2, 3])

    # Set axis limits
    ax.set_xlim(0- 0.5, cols - 0.5)
    ax.set_ylim(0- 0.5, rows - 0.5)
    ax.set_zlim(0, layers * layer_spacing - 1)

    # # Invert z-axis 
    # ax.invert_zaxis()

    # Show plot
    plt.show()



    #--------------------------------------------------------------------------------------------------------
    # Sample data generation
    layers = 4  # Number of layers
    rows = 4    # Number of rows per layer
    cols = 4    # Number of columns per layer

    # data = np.random.rand(layers, rows, cols)

    # Set up the figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Customize the colormap
    # cmap = plt.get_cmap('viridis')

    # colors_list = ['#cfd4e4', '#9aabe0', '#647ed3', '#3a5fd5'] 
    colors_list = ['#9af8fd', '#02d6e1', 'blue', 'darkblue'] 
    cmap = colors.ListedColormap(colors_list)

    # Function to create a square at a given position
    def create_square(x, y, z, value):
        square = [
            [x - 0.5, y- 0.5, z],
            [x + 1- 0.5, y- 0.5, z],
            [x + 1- 0.5, y + 1- 0.5, z],
            [x- 0.5, y + 1- 0.5, z]
        ]
        return square
    
    def get_color(z, y, x):
        if ((z + y + x) % 2 == 1):
            return "black"
        elif z == 0:
            return "cyan"
        elif z == 1:
            return "purple"
        elif z == 2:
            return "yellow"
        elif z == 3:
            return "red"
        else:
            print("HUHUHUHUHU???????????????")
            return "black"
        
    # Define the spacing between layers
    layer_spacing = 1

    # Loop through each layer and plot flat squares
    for z in range(layers):
        for y in range(rows):
            for x in range(cols):
                value = data[z, y, x]
                square = create_square(x, y, z * layer_spacing, value)
                color = get_color(z, y, x)
                poly = Poly3DCollection([square], color=color, alpha=0.75)
                ax.add_collection3d(poly)
                # ax.text(x, y, z * layer_spacing + 0.3, f'{value:.2f}', color='black', ha='center', va='center')

    # Set labels
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    ax.set_zlabel('Z coordinate')

    # Set title
    # ax.set_title('Average Manhattan Distance of cores in 4x4x4 network')


    # Customize the colorbar
    norm = plt.Normalize(data.min() -0.25, data.max() +0.25)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Hide grid lines
    ax.grid(False)

    legend_elements = [Patch(facecolor='black', label='Non active'),
                    Patch(facecolor='cyan', label='Task 0'),
                    Patch(facecolor='purple', label='Task 1'),
                    Patch(facecolor='yellow', label='Task 2'),
                    Patch(facecolor='red', label='Task 3')]

    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.4, 1.05))
    
    # Set axis ticks and labels
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels([0, 1, 2, 3])
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels([0, 1, 2, 3])
    ax.set_zticks([0, 1, 2, 3])
    ax.set_zticklabels([0, 1, 2, 3])

    # Set axis limits
    ax.set_xlim(0- 0.5, cols - 0.5)
    ax.set_ylim(0- 0.5, rows - 0.5)
    ax.set_zlim(0, layers * layer_spacing - 1)

    # Show plot
    plt.show()