sample_dict = {
    "hello": { "content": "Hello, world!", "type": "file" },
    "sub": {
        "type": "directory",
        "content": {
            "file1": { "content": "File 1 content", "type": "file" },
            "file2": { "content": "File 2 content", "type": "file" },
            "subsub": {
                "type": "directory",
                "content": {
                    "file3": { "content": "File 3 content", "type": "file" }
                }
            }
        }
    },
    "Ok": { "content": "OK!", "type": "file" }
}
def modify_nested_dict(tree, keys, new_value):
    if len(keys) == 1:
        tree[keys[0]] = new_value
    else:
        modify_nested_dict(tree[keys[0]], keys[1:], new_value)

# Example usage:



keys_to_modify = ['sub','content','subsub','content','fileNew']
new_value = { "content": "File New content", "type": "file" }

modify_nested_dict(sample_dict, keys_to_modify, new_value)

print(sample_dict)



