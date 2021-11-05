import singer

LOGGER = singer.get_logger()

class Stream:
    """Stream class to create stream source objects."""

    # Create default class variables 
    stream_id = None
    key_properties = []
    replication_method = ""
    valid_replication_keys = []
    replication_key = None
    object_type = ""

    # Create __init__() constructor for class
    def __init__(self, client, state):
        self.client = client
        self.state = state


class EmployeeDirectory(Stream):
    """Create class for stream EmployeeDirectory from source
    that inherits from Stream class."""

    # Set variable names for stream - modify here if required
    stream_id = "employee_directory"
    key_properties = ["id"]
    object_type = "EMPLOYEE_DIRECTORY"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        employee_directory = self.client.fetch_employee_directory()
        for employeed in employee_directory:
            yield employeed      


class Employee(Stream):
    """Create class for stream Employee_id from source
    that inherits from Stream class. Returns single employee id with
    custom selected fields"""

    # Set variable names for stream - modify here if required
    stream_id = "employee_id"
    key_properties = ["id"]
    object_type = "EMPLOYEE_ID"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        employee_id = self.client.fetch_employee_id()
        yield employee_id


# class AllEmployees(Stream):
#     """Create class for stream AllEmployees from source
#     that inherits from Stream class."""

#     # Set variable names for stream - modify here if required
#     stream_id = "employee_directory"
#     key_properties = ["id"]
#     object_type = "ALL_EMPLOYEES"
#     replication_method = "FULL_TABLE"
#     valid_replication_keys = ["id"]
#     replication_key = "id"
#     selected = False

#     # Define sync function to get stream data per line
#     def sync(self, *args, **kwargs):
#         all_employees = self.client.fetch_all_employees()
#         for employee in all_employees:
#             yield employee


class WhosOut(Stream):
    """Create class for stream WhosOut from source
    that inherits from Stream class"""

    # Set variable name for stream - modify here if required
    stream_id = "whos_out"
    key_properties = ["employeeId"]
    object_type = "WHOS_OUT"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["employeeId"]
    replication_key = "employeeId"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        whos_out = self.client.fetch_whos_out()
        for who_out in whos_out:
            yield who_out


class MetaFields(Stream):
    """Create class for stream MetaFields from source
    that inherits from Stream class"""
    
    # Set variable name for stream - modify here if required
    stream_id = "meta_fields"
    key_properties = ["id"]
    object_type = "META_FIELDS"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        meta_fields = self.client.fetch_meta_fields()
        for meta_field in meta_fields:
            yield meta_field


class TimeOffPolicies(Stream):
    """Create class for stream TimeOffPolicies from source
    that inherits from Stream class"""

    # Set variable name for stream - modify here if required
    stream_id = "time_off_policies"
    key_properties = ["id"]
    object_type = "TIME_OFF_POLICIES"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        time_off_policies = self.client.fetch_time_off_policies()
        for time_off_policiy in time_off_policies:
            yield time_off_policiy        

        
class BenDedTypes(Stream):
    """Create class for stream Benefits Deduction Types from source
    that inherits from Stream class"""
    
    # Set variable name for stream - modify here if required
    stream_id = "benefit_deduction_types"
    key_properties = ["id"]
    object_type = "BEN_DED_TYPES"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        ben_ded_types = self.client.fetch_benefit_deduc_types()
        for ben_ded_type in ben_ded_types:
            yield ben_ded_type


class BenCoverages(Stream):
    """Create class for stream Benefits Coverages from source
    that inherits from Stream class"""
    
    # Set variable name for stream - modify here if required
    stream_id = "benefit_coverages"
    key_properties = ["id"]
    object_type = "BEN_COVERAGES"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    ## FIX nested json response
    def sync(self, *args, **kwargs):
        ben_coverages = self.client.fetch_benefit_coverages()
        yield ben_coverages
        # for ben_coverage in ben_coverages:
        #     yield ben_coverage


class EmployeeDependents(Stream):
    """Create class for stream Employee Dependents from source
    that inherits from Stream class"""
    
    # Set variable name for stream - modify here if required
    stream_id = "employee_dependents"
    key_properties = ["id"]
    object_type = "EMPL_DEPEND"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        empl_depends = self.client.fetch_empl_dependents()
        for empl_depend in empl_depends["Employee Dependents"]:
            yield empl_depend


class BenefitPlans(Stream):
    """Create class for stream Benefit Plans from source
    that inherits from Stream class"""

    # Set variable name for stream - modify here if required
    stream_id = "benefit_plans"
    key_properties = ["id"]
    object_type = "BEN_PLANS"
    replication_method =  "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        benefit_plans = self.client.fetch_benefit_plans()
        for benefit_plan in benefit_plans["Benefit Plans"]:
            yield benefit_plan


class BenefitGroups(Stream):
    """Create class for stream Benefit Groups from source
    that inherits from Stream class"""

    # Set variable name for stream - modify here if required
    stream_id = "benefit_groups"
    key_properties = ["id"]
    object_type = "BEN_GROUPS"
    replication_method =  "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        benefit_groups = self.client.fetch_benefit_groups()
        for benefit_group in benefit_groups["Benefit Groups"]:
            yield benefit_group


class TrainingTypes(Stream):
    """Create class for stream Training Types from source
    that inherits from Stream class"""
    
    # Set variable name for stream - modify here if required
    stream_id = "training_types"
    key_properties = ["id"]
    object_type = "TRAINING_TYPES"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    ## FIX nested json response
    def sync(self, *args, **kwargs):
        training_types = self.client.fetch_training_types()
        yield training_types
        # for training_type in training_types:
        #     yield training_type.value()


class TrainingCategories(Stream):
    """Create class for stream Training Categories from source
    that inherits from Stream class"""
    
    # Set variable name for stream - modify here if required
    stream_id = "training_categories"
    key_properties = ["id"]
    object_type = "TRAINING_CATEGORIES"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    ## FIX nested json response
    def sync(self, *args, **kwargs):
        training_cats = self.client.fetch_training_categories()
        yield training_cats
        # for training_cat in training_cats:
        #     yield training_cat
    

# Dictionary containing all streams available.
STREAMS = {
    "employees": EmployeeDirectory,
    "employee" : Employee,
    "whos_out": WhosOut,
    "meta_fields": MetaFields,
    "time_off_policies": TimeOffPolicies,
    "benefit_deduc_types": BenDedTypes,
    "benefit_coverages": BenCoverages,
    "employee_dependents": EmployeeDependents,
    "benefit_plans": BenefitPlans,
    "benefit_groups": BenefitGroups,
    "training_types": TrainingTypes,
    "training_categories": TrainingCategories
}
