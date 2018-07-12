"""Generated client library for alpha_vision version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.alpha_vision.v1 import alpha_vision_v1_messages as messages


class AlphaVisionV1(base_api.BaseApiClient):
  """Generated client library for service alpha_vision version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://alpha-vision.googleapis.com/'

  _PACKAGE = u'alpha_vision'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-vision']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'AlphaVisionV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new alpha_vision handle."""
    url = url or self.BASE_URL
    super(AlphaVisionV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.files = self.FilesService(self)
    self.images = self.ImagesService(self)
    self.locations_operations = self.LocationsOperationsService(self)
    self.locations = self.LocationsService(self)
    self.operations = self.OperationsService(self)
    self.projects_locations_productSets_products = self.ProjectsLocationsProductSetsProductsService(self)
    self.projects_locations_productSets = self.ProjectsLocationsProductSetsService(self)
    self.projects_locations_products_referenceImages = self.ProjectsLocationsProductsReferenceImagesService(self)
    self.projects_locations_products = self.ProjectsLocationsProductsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class FilesService(base_api.BaseApiService):
    """Service class for the files resource."""

    _NAME = u'files'

    def __init__(self, client):
      super(AlphaVisionV1.FilesService, self).__init__(client)
      self._upload_configs = {
          }

    def AsyncBatchAnnotate(self, request, global_params=None):
      r"""Run asynchronous image detection and annotation for a list of generic.
files, such as PDF files, which may contain multiple pages and multiple
images per page. Progress and results can be retrieved through the
`google.longrunning.Operations` interface.
`Operation.metadata` contains `OperationMetadata` (metadata).
`Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

      Args:
        request: (AsyncBatchAnnotateFilesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AsyncBatchAnnotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    AsyncBatchAnnotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'alpha_vision.files.asyncBatchAnnotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/files:asyncBatchAnnotate',
        request_field='<request>',
        request_type_name=u'AsyncBatchAnnotateFilesRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ImagesService(base_api.BaseApiService):
    """Service class for the images resource."""

    _NAME = u'images'

    def __init__(self, client):
      super(AlphaVisionV1.ImagesService, self).__init__(client)
      self._upload_configs = {
          }

    def Annotate(self, request, global_params=None):
      r"""Run image detection and annotation for a batch of images.

      Args:
        request: (BatchAnnotateImagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchAnnotateImagesResponse) The response message.
      """
      config = self.GetMethodConfig('Annotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Annotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'alpha_vision.images.annotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/images:annotate',
        request_field='<request>',
        request_type_name=u'BatchAnnotateImagesRequest',
        response_type_name=u'BatchAnnotateImagesResponse',
        supports_download=False,
    )

  class LocationsOperationsService(base_api.BaseApiService):
    """Service class for the locations_operations resource."""

    _NAME = u'locations_operations'

    def __init__(self, client):
      super(AlphaVisionV1.LocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (AlphaVisionLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'alpha_vision.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionLocationsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class LocationsService(base_api.BaseApiService):
    """Service class for the locations resource."""

    _NAME = u'locations'

    def __init__(self, client):
      super(AlphaVisionV1.LocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(AlphaVisionV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (AlphaVisionOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'alpha_vision.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'AlphaVisionOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (AlphaVisionOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'alpha_vision.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (AlphaVisionOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'alpha_vision.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (AlphaVisionOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations',
        http_method=u'GET',
        method_id=u'alpha_vision.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsProductSetsProductsService(base_api.BaseApiService):
    """Service class for the projects_locations_productSets_products resource."""

    _NAME = u'projects_locations_productSets_products'

    def __init__(self, client):
      super(AlphaVisionV1.ProjectsLocationsProductSetsProductsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the Products in a ProductSet, in an unspecified order. If the.
ProductSet does not exist, the products field of the response will be
empty.

Possible errors:

* Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsProductsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProductsInProductSetResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets/{productSetsId}/products',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.productSets.products.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}/products',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsProductsListRequest',
        response_type_name=u'ListProductsInProductSetResponse',
        supports_download=False,
    )

  class ProjectsLocationsProductSetsService(base_api.BaseApiService):
    """Service class for the projects_locations_productSets resource."""

    _NAME = u'projects_locations_productSets'

    def __init__(self, client):
      super(AlphaVisionV1.ProjectsLocationsProductSetsService, self).__init__(client)
      self._upload_configs = {
          }

    def AddProduct(self, request, global_params=None):
      r"""Adds a Product to the specified ProductSet. If the Product is already.
present, no change is made.

One Product can be added to at most 100 ProductSets.

Possible errors:

* Returns NOT_FOUND if the Product or the ProductSet doesn't exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsAddProductRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('AddProduct')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddProduct.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets/{productSetsId}:addProduct',
        http_method=u'POST',
        method_id=u'alpha_vision.projects.locations.productSets.addProduct',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:addProduct',
        request_field=u'addProductToProductSetRequest',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsAddProductRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates and returns a new ProductSet resource.

Possible errors:

* Returns INVALID_ARGUMENT if display_name is missing, or is longer than
  4096 characters.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProductSet) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets',
        http_method=u'POST',
        method_id=u'alpha_vision.projects.locations.productSets.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'productSetId'],
        relative_path=u'v1/{+parent}/productSets',
        request_field=u'productSet',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsCreateRequest',
        response_type_name=u'ProductSet',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Permanently deletes a ProductSet. All Products and ReferenceImages in the.
ProductSet will be deleted.

The actual image files are not deleted from Google Cloud Storage.

Possible errors:

* Returns NOT_FOUND if the ProductSet does not exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets/{productSetsId}',
        http_method=u'DELETE',
        method_id=u'alpha_vision.projects.locations.productSets.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information associated with a ProductSet.

Possible errors:

* Returns NOT_FOUND if the ProductSet does not exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProductSet) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets/{productSetsId}',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.productSets.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsGetRequest',
        response_type_name=u'ProductSet',
        supports_download=False,
    )

    def Import(self, request, global_params=None):
      r"""Asynchronous API that imports a list of reference images to specified.
product sets based on a list of image information.

The google.longrunning.Operation API can be used to keep track of the
progress and results of the request.
`Operation.metadata` contains `BatchOperationMetadata`. (progress)
`Operation.response` contains `ImportProductSetsResponse`. (results)

The input source of this method is a csv file on Google Cloud Storage.
For the format of the csv file please see
ImportProductSetsGcsSource.csv_file_uri.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    Import.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets:import',
        http_method=u'POST',
        method_id=u'alpha_vision.projects.locations.productSets.import',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/productSets:import',
        request_field=u'importProductSetsRequest',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsImportRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists ProductSets in an unspecified order.

Possible errors:

* Returns INVALID_ARGUMENT if page_size is greater than 100, or less
  than 1.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProductSetsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.productSets.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/productSets',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsListRequest',
        response_type_name=u'ListProductSetsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Makes changes to a ProductSet resource.
Only display_name can be updated currently.

Possible errors:

* Returns NOT_FOUND if the ProductSet does not exist.
* Returns INVALID_ARGUMENT if display_name is present in update_mask but
  missing from the request or longer than 4096 characters.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProductSet) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets/{productSetsId}',
        http_method=u'PATCH',
        method_id=u'alpha_vision.projects.locations.productSets.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'productSet',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsPatchRequest',
        response_type_name=u'ProductSet',
        supports_download=False,
    )

    def RemoveProduct(self, request, global_params=None):
      r"""Removes a Product from the specified ProductSet.

Possible errors:

* Returns NOT_FOUND If the Product is not found under the ProductSet.

      Args:
        request: (AlphaVisionProjectsLocationsProductSetsRemoveProductRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('RemoveProduct')
      return self._RunMethod(
          config, request, global_params=global_params)

    RemoveProduct.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/productSets/{productSetsId}:removeProduct',
        http_method=u'POST',
        method_id=u'alpha_vision.projects.locations.productSets.removeProduct',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:removeProduct',
        request_field=u'removeProductFromProductSetRequest',
        request_type_name=u'AlphaVisionProjectsLocationsProductSetsRemoveProductRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

  class ProjectsLocationsProductsReferenceImagesService(base_api.BaseApiService):
    """Service class for the projects_locations_products_referenceImages resource."""

    _NAME = u'projects_locations_products_referenceImages'

    def __init__(self, client):
      super(AlphaVisionV1.ProjectsLocationsProductsReferenceImagesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates and returns a new ReferenceImage resource.

The `bounding_poly` field is optional. If `bounding_poly` is not specified,
the system will try to detect regions of interest in the image that are
compatible with the product_category on the parent product. If it is
specified, detection is ALWAYS skipped. The system converts polygons into
non-rotated rectangles.

Note that the pipeline will resize the image if the image resolution is too
large to process (above 50MP).

Possible errors:

* Returns INVALID_ARGUMENT if the image_uri is missing or longer than 4096
  characters.
* Returns INVALID_ARGUMENT if the product does not exist.
* Returns INVALID_ARGUMENT if bounding_poly is not provided, and nothing
  compatible with the parent product's product_category is detected.
* Returns INVALID_ARGUMENT if bounding_poly contains more than 10 polygons.

      Args:
        request: (AlphaVisionProjectsLocationsProductsReferenceImagesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReferenceImage) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}/referenceImages',
        http_method=u'POST',
        method_id=u'alpha_vision.projects.locations.products.referenceImages.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'referenceImageId'],
        relative_path=u'v1/{+parent}/referenceImages',
        request_field=u'referenceImage',
        request_type_name=u'AlphaVisionProjectsLocationsProductsReferenceImagesCreateRequest',
        response_type_name=u'ReferenceImage',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Permanently deletes a reference image.

The image metadata will be deleted right away, but search queries
against ProductSets containing the image may still work until all related
caches are refreshed.

The actual image files are not deleted from Google Cloud Storage.

Possible errors:

* Returns NOT_FOUND if the reference image does not exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductsReferenceImagesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}/referenceImages/{referenceImagesId}',
        http_method=u'DELETE',
        method_id=u'alpha_vision.projects.locations.products.referenceImages.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductsReferenceImagesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information associated with a ReferenceImage.

Possible errors:

* Returns NOT_FOUND if the specified image does not exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductsReferenceImagesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReferenceImage) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}/referenceImages/{referenceImagesId}',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.products.referenceImages.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductsReferenceImagesGetRequest',
        response_type_name=u'ReferenceImage',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists reference images.

Possible errors:

* Returns NOT_FOUND if the parent product does not exist.
* Returns INVALID_ARGUMENT if the page_size is greater than 100, or less
  than 1.

      Args:
        request: (AlphaVisionProjectsLocationsProductsReferenceImagesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListReferenceImagesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}/referenceImages',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.products.referenceImages.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/referenceImages',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductsReferenceImagesListRequest',
        response_type_name=u'ListReferenceImagesResponse',
        supports_download=False,
    )

  class ProjectsLocationsProductsService(base_api.BaseApiService):
    """Service class for the projects_locations_products resource."""

    _NAME = u'projects_locations_products'

    def __init__(self, client):
      super(AlphaVisionV1.ProjectsLocationsProductsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates and returns a new product resource.

Possible errors:

* Returns INVALID_ARGUMENT if display_name is missing or longer than 4096
  characters.
* Returns INVALID_ARGUMENT if description is longer than 4096 characters.
* Returns INVALID_ARGUMENT if product_category is missing or invalid.

      Args:
        request: (AlphaVisionProjectsLocationsProductsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Product) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products',
        http_method=u'POST',
        method_id=u'alpha_vision.projects.locations.products.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'productId'],
        relative_path=u'v1/{+parent}/products',
        request_field=u'product',
        request_type_name=u'AlphaVisionProjectsLocationsProductsCreateRequest',
        response_type_name=u'Product',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Permanently deletes a product and its reference images.

Metadata of the product and all its images will be deleted right away, but
search queries against ProductSets containing the product may still work
until all related caches are refreshed.

Possible errors:

* Returns NOT_FOUND if the product does not exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}',
        http_method=u'DELETE',
        method_id=u'alpha_vision.projects.locations.products.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets information associated with a Product.

Possible errors:

* Returns NOT_FOUND if the Product does not exist.

      Args:
        request: (AlphaVisionProjectsLocationsProductsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Product) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.products.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductsGetRequest',
        response_type_name=u'Product',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists products in an unspecified order.

Possible errors:

* Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.

      Args:
        request: (AlphaVisionProjectsLocationsProductsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListProductsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products',
        http_method=u'GET',
        method_id=u'alpha_vision.projects.locations.products.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/products',
        request_field='',
        request_type_name=u'AlphaVisionProjectsLocationsProductsListRequest',
        response_type_name=u'ListProductsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Makes changes to a Product resource.
Only display_name, description and labels can be updated right now.

If labels are updated, the change will not be reflected in queries until
the next index time.

Possible errors:

* Returns NOT_FOUND if the Product does not exist.
* Returns INVALID_ARGUMENT if display_name is present in update_mask but is
  missing from the request or longer than 4096 characters.
* Returns INVALID_ARGUMENT if description is present in update_mask but is
  longer than 4096 characters.
* Returns INVALID_ARGUMENT if product_category is present in update_mask.

      Args:
        request: (AlphaVisionProjectsLocationsProductsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Product) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/products/{productsId}',
        http_method=u'PATCH',
        method_id=u'alpha_vision.projects.locations.products.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'product',
        request_type_name=u'AlphaVisionProjectsLocationsProductsPatchRequest',
        response_type_name=u'Product',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(AlphaVisionV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(AlphaVisionV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }