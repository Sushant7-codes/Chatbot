def tokenize(message):
    
    message = message.lower().strip()
    tokens = message.split()
    
    tokens = [token.strip() for token in tokens]
    
    tokens = [token.strip('.,!?;()[]{}"\'') for token in tokens]
    
    return tokens