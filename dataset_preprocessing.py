# preprocessing del dataset
import pandas as pd


def processed_dataset():
    """
        Preprocessa il dataset che si trova in ./csv
            args:
                niente
            return:
                nulla, salva il dataset in ./processed_dataset/flipkart_dataset.csv

        """
    dataset_flipkart = pd.read_csv("csv/flipkart_com-ecommerce_sample.csv")

    colonne_da_rimuovere_flipkart = ["uniq_id", "crawl_timestamp", "product_url", "pid", "retail_price",
                                     "discounted_price", "is_FK_Advantage_product", "product_rating", "overall_rating"]

    dataset_flipkart.drop(columns=colonne_da_rimuovere_flipkart, inplace=True)

    # Filtra le righe in cui la colonna 'product_category_tree' contiene la parola 'clothing'
    dataset_flipkart = dataset_flipkart[~dataset_flipkart['product_category_tree'].str.contains('clothing', case=False)]
    dataset_flipkart = dataset_flipkart[~dataset_flipkart['product_category_tree'].str.contains('women', case=False)]
    dataset_flipkart = dataset_flipkart[
        ~dataset_flipkart['product_category_tree'].str.contains('Jewellery|jewels', case=False)]
    dataset_flipkart = dataset_flipkart[
        ~dataset_flipkart['product_category_tree'].str.contains('Home Decor|sticker', case=False)]
    dataset_flipkart = dataset_flipkart[~dataset_flipkart['product_category_tree'].str.contains('beauty', case=False)]
    dataset_flipkart = dataset_flipkart[~dataset_flipkart['product_category_tree'].str.contains('footwear', case=False)]
    dataset_flipkart = dataset_flipkart[
        ~dataset_flipkart['product_category_tree'].str.contains(
            'Home furnishing|cases|mat|cover|art|pet|glasses|plant|watch|router|garden', case=False)]
    dataset_flipkart = dataset_flipkart[
        ~dataset_flipkart['product_category_tree'].str.contains('Kitchen & Dining|baby|babies ', case=False)]
    dataset_flipkart = dataset_flipkart[
        ~dataset_flipkart['product_category_tree'].str.contains('bag|bags|Bootwale Bellies|seed|school|sofa',
                                                                case=False)]

    print("rows rimaste dopo il preprocessing nel dataset:", len(dataset_flipkart))
    dataset_flipkart.to_csv("processed_dataset/flipkart_dataset.csv", index=False)

    return dataset_flipkart
