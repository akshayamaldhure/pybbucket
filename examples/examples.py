import pybbucket.log as logger
from pybbucket.bitbucket import Bitbucket
from pybbucket.bitbucket_repository import BitbucketRepository
from pybbucket.bitbucket_user import BitbucketUser

if __name__ == '__main__':
    log = logger.setup_custom_logger('root')
    bitbucket = Bitbucket(api_server_url="https://api.bitbucket.org/", workspace_id="your_workspace_id",
                          username="your_bitbucket_username", password="your_bitbucket_password")
    # Example-1
    test_username = "test_user@domain.com"
    bitbucket_user = BitbucketUser(bitbucket=bitbucket, username=test_username)
    display_name = bitbucket_user.get_user_details().json()['display_name']
    log.info("Display name for {} is {}".format(test_username, display_name))
    # Example-2
    repository_name = "your_repository_name"
    bitbucket_repository = BitbucketRepository(bitbucket=bitbucket, repository_name=repository_name)
    branch_names = [x['name'] for x in bitbucket_repository.get_branches().json()['values']]
    log.info("Branches in the repository {} are {}".format(repository_name, str(branch_names)))
