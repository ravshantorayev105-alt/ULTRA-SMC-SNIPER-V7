import matplotlib.pyplot as plt

def chart(df,pair):

    plt.figure(figsize=(6,4))

    plt.plot(df.close)

    file=f"{pair}.png"

    plt.title(pair)

    plt.savefig(file)

    plt.close()

    return file
