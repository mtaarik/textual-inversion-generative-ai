import os
from PIL import Image

def prepare_dataset(input_dir, output_dir, target_size=(512, 512)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Liste tous les fichiers dans le dossier raw
    valid_extensions = ('.png', '.jpg', '.jpeg', '.webp')
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(valid_extensions):
            filepath = os.path.join(input_dir, filename)
            
            try:
                with Image.open(filepath) as img:
                    # Convertir en RGB
                    img = img.convert("RGB")
                    
                    # Calcul pour le recadrage
                    width, height = img.size
                    new_size = min(width, height)
                    
                    left = (width - new_size) / 2
                    top = (height - new_size) / 2
                    right = (width + new_size) / 2
                    bottom = (height + new_size) / 2
                    
                    img_cropped = img.crop((left, top, right, bottom))
                    
                    # Redimensionnement (512x512)
                    img_resized = img_cropped.resize(target_size, Image.Resampling.LANCZOS)
                    
                    # Sauvegarde
                    output_path = os.path.join(output_dir, f"processed_{filename}")
                    img_resized.save(output_path, "JPEG", quality=95)
                    print(f" Succès : {filename} -> processed_{filename}")
                    
            except Exception as e:
                print(f" Erreur avec {filename}: {e}")

if __name__ == "__main__":
    # Calcul des chemins absolus pour éviter les erreurs selon d'où on lance le script
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_DIR = os.path.join(BASE_DIR, "dataset", "raw")
    PROCESSED_DIR = os.path.join(BASE_DIR, "dataset", "processed")
    
    print("Début du traitement des images...")
    prepare_dataset(RAW_DIR, PROCESSED_DIR)
    print("\nTerminé ! Va vérifier le dossier dataset/processed/")
