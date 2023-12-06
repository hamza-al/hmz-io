def update_nested_dict(d, keys, value):
    current_dict = d

    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})

    current_dict[keys[-1]] = value

# Example usage
nested_dict = {
  "hello": { "content": "", "type": "file" },
  "sub": { "type": "directory", "content": {
      "hello.txt": { "content": "", "type": "file" },
      "sub": { "type": "directory", "content": {} }
  } }
}

keys_list = ['sub','sub']
new_value = {"example": "new_value"}

update_nested_dict(nested_dict, keys_list, new_value)

print(nested_dict)
