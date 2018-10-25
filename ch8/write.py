poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

if __name__ == "__main__":
    # file open
    fout = open('relativity', 'wt')
    # write
    print(fout.write(poem))
    # file close
    fout.close()