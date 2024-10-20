from transformers import GPT2LMHeadModel, GPT2Tokenizer, BertTokenizer
import torch
from tqdm import tqdm  # 导入 tqdm 库

# 加载 GPT-2 预训练模型和对应的 tokenizer
model_name = "uer/gpt2-chinese-cluecorpussmall"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Add a padding token explicitly
tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Make sure to resize the token embeddings of the model to match the new tokens added to the tokenizer
model.resize_token_embeddings(len(tokenizer))

# 微调数据集：使用您预处理好的诗歌数据
def train_gpt2_model(poems):
    # 将模型移动到 GPU（如果可用）
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"使用设备: {device}")
    model.to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

    # 定义训练参数
    model.train()
    batch_size = 4  # 您可以调整批次大小，如果出现显存不足可以尝试减小
    num_epochs = 10

    print("开始训练...")
    for epoch in range(num_epochs):
        total_loss = 0
        print(f"\nEpoch {epoch+1}/{num_epochs}")
        # 使用 tqdm 包装数据加载循环，添加进度条
        for i in tqdm(range(0, len(poems), batch_size), desc="训练进度"):
            batch = poems[i:i+batch_size]
            inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)
            outputs = model(**inputs, labels=inputs["input_ids"])
            loss = outputs.loss
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / (len(poems) / batch_size)
        print(f"Epoch {epoch+1}/{num_epochs} - 平均损失: {avg_loss:.4f}")

# 定义函数来加载和处理数据
def load_and_preprocess_poems(file_path):
    poems = []
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取整个文件
        content = file.read()
        content = content.replace('�', '')
        # 根据文件分割符分开每一首诗
        raw_poems = content.split('====文件分割符====')

        for raw_poem in raw_poems:
            # 清理每首诗中的内容，去除多余的空行和 '|' 符号
            poem = raw_poem.strip().replace('|', '\n')
            if poem:  # 如果内容不为空
                poems.append(poem)
    return poems

# 上传并加载诗歌数据文件
file_path = r".\poetry-generator\backend\output.txt"  # 获取文件路径

# 预处理诗歌数据
poems = load_and_preprocess_poems(file_path)
print(f"共加载了 {len(poems)} 首诗歌。")

# 现在将处理好的诗歌列表传递给模型进行训练
print("开始微调 GPT-2 模型...")
train_gpt2_model(poems)

# 保存微调后的模型和 tokenizer
model.save_pretrained(r".\poetry-generator\backend\models\fine_tuned_model_2")
tokenizer.save_pretrained(r".\poetry-generator\backend\models\fine_tuned_model_2")
