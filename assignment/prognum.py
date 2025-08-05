# prognum.py
# フィボナッチ数列を計算する再帰的な関数を定義
def fibonacci(n):
    """
    指定されたn番目のフィボナッチ数を再帰的に計算する関数。
    
    Args:
        n (int): 求めたいフィボナッチ数の番目。

    Returns:
        int: n番目のフィボナッチ数。
    """
    # 1番目と2番目のフィボナッチ数は1
    if n <= 2:
        return 1
    
    # n番目のフィボナッチ数は、直前の2つの数の和
    # ここで関数自身を呼び出すことで再帰的な処理を実現
    return fibonacci(n - 1) + fibonacci(n - 2)
