from data_loader import load_datasets

train_ds, val_ds, test_ds, class_names = load_datasets("fish")

print("\nClasses:")
print(class_names)