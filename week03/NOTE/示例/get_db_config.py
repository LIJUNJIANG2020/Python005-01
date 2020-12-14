from configparser import ConfigParser

def get_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return dict(items)

if __name__ == '__main__':
    print(get_db_config())
