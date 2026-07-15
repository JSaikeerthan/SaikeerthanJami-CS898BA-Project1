from data_loader import load_datasets
from model import build_model
from trainer import train_model

# Load datasets
train_ds, val_ds, test_ds, class_names = load_datasets("fish")

print("\nClasses:")
print(class_names)

# Build CNN
model = build_model(
    len(class_names)
)

model.summary()

# Train baseline model
history = train_model(
    model,
    train_ds,
    val_ds,
    epochs=20
)