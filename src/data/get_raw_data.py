
import os
from dotenv import find_dotenv, load_dotenv
from requests import session
import logging

payload = {
    'action': 'login',
    'username': os.environ.get("KAGGLE_USERNAME"),
    'password': os.environ.get("KAGGLE_PASSWORD")
}

def extract_data(url, file_path):
    '''
    method to extract data
    '''
    with session() as c:
        c.post('https://www.kaggle.com/account/login', data=payload)
        with open(file_path, 'w') as handle:
            response = c.get(url, stream=True)
            for block in response.iter_content(1024):
                handle.write(block)
                
def main(project_dir):
    '''
    main method
    '''
    
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    train_url = 'https://www.kaggle.com/c/titanic/download/train.csv'
    test_url = 'https://www.kaggle.com/c/titanic/download/test.csv'

    raw_data_path = os.path.join(project_dir, 'data', 'raw')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')

    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)
    
    logger.info('downloaded raw training and test data')
    

if __name__ == '_main_':
    project_dir = os.path.join(os.path.dirname(_file_), os.pardir, os.pardir)
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    main(project_dir)
    