class APIResponseCode(object):
    FAILURE = (-1, 'General failure')  # General logic error
    SUCCESS = (0, 'Success')  # Successful response
    SERVER_ERROR = (1, 'Server error')  # Unexpected error during handling the request
    BAD_REQUEST = (2, 'Bad request')  # Error returned by DRF serializer
    NO_PERMISSION = (3, 'No permission')  # Error related to permissions
    NOT_FOUND = (4, 'Not found')  # Object not found
    ALREADY_EXISTS = (5, 'Already exists')  # Object already exists
    VALIDATION_ERROR = (6, 'Validation error')  # Error related to invalidated input
    INVALID_ACTION = (7, 'Invalid request')  # Invalid action (stateful)
    ACTION_DENIED = (8, 'Action denied')  # Invalid action (stateless)
    FILE_ERROR = (9, 'File error')  # Error related to file handling
    DB_ERROR = (10, 'Database error')  # Error related to database
    EXT_API_ERROR = (11, 'External API error')  # Error related to calling external API
    TIMEOUT = (12, 'Timeout')  # Timeout when handling a request
    EXPIRED = (13, 'Request expired')
    TOO_MANY_REQUEST = (14, 'Too many request')
    INSUFFICIENT_BALANCE = (15, 'Insufficient balance')
    REWARD_ALREADY_CLAIMED = (16, 'reward already claimed')
    OUT_OF_SLOT = (17, 'out of slot')
    ALREADY_SAVED = (18, 'already saved')
    MAX_RETRY_EXCEEDED = (19, 'max retries exceeded')
    OUT_OF_GIFT = (20, 'out of gift')

    @classmethod
    def is_success(cls, code):
        return code == cls.SUCCESS

    @classmethod
    def is_failure(cls, code):
        return code != cls.SUCCESS