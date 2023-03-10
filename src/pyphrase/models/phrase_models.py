from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, confloat, conint, constr


class Model(BaseModel):
    __root__: Any


class Role(Enum):
    SYS_ADMIN = "SYS_ADMIN"
    SYS_ADMIN_READ = "SYS_ADMIN_READ"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LINGUIST = "LINGUIST"
    GUEST = "GUEST"
    SUBMITTER = "SUBMITTER"


class UserReference(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    userName: Optional[str] = None
    email: Optional[str] = None
    role: Optional[Role] = None
    id: Optional[str] = None
    uid: Optional[str] = None


class AdditionalWorkflowStepDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class AdditionalWorkflowStepRequestDto(BaseModel):
    name: constr(min_length=0, max_length=255) = Field(
        ..., description="Name of the additional workflow step"
    )


class PageDtoAdditionalWorkflowStepDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[AdditionalWorkflowStepDto]] = None


class Action(Enum):
    PRE_ANALYSE = "PRE_ANALYSE"
    POST_ANALYSE = "POST_ANALYSE"
    COMPARE_ANALYSE = "COMPARE_ANALYSE"
    PARENT_ANALYSE = "PARENT_ANALYSE"
    PRE_TRANSLATE = "PRE_TRANSLATE"
    ASYNC_TRANSLATE = "ASYNC_TRANSLATE"
    IMPORT_JOB = "IMPORT_JOB"
    IMPORT_FILE = "IMPORT_FILE"
    ALIGN = "ALIGN"
    EXPORT_TMX_BY_QUERY = "EXPORT_TMX_BY_QUERY"
    EXPORT_TMX = "EXPORT_TMX"
    IMPORT_TMX = "IMPORT_TMX"
    INSERT_INTO_TM = "INSERT_INTO_TM"
    DELETE_TM = "DELETE_TM"
    CLEAR_TM = "CLEAR_TM"
    QA = "QA"
    QA_V3 = "QA_V3"
    UPDATE_CONTINUOUS_JOB = "UPDATE_CONTINUOUS_JOB"
    UPDATE_SOURCE = "UPDATE_SOURCE"
    UPDATE_TARGET = "UPDATE_TARGET"
    EXTRACT_CLEANED_TMS = "EXTRACT_CLEANED_TMS"
    GLOSSARY_PUT = "GLOSSARY_PUT"
    GLOSSARY_DELETE = "GLOSSARY_DELETE"
    CREATE_PROJECT = "CREATE_PROJECT"
    EXPORT_COMPLETE_FILE = "EXPORT_COMPLETE_FILE"


class ErrorDetailDto(BaseModel):
    code: Optional[str] = Field(None, description="Code, e.g. NOT_FOUND.")
    args: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description='Related arguments, e.g. number => "hello world"'
    )
    message: Optional[str] = Field(None, description="Optional human-readable message.")


class ObjectReference(BaseModel):
    pass


class IdReference(BaseModel):
    id: str


class UidReference(BaseModel):
    uid: str


class AnalyseJobReference(BaseModel):
    uid: Optional[str] = None
    filename: Optional[str] = None
    innerId: Optional[str] = None


class CountsDto(BaseModel):
    segments: Optional[float] = None
    words: Optional[float] = None
    characters: Optional[float] = None
    normalizedPages: Optional[float] = None
    percent: Optional[float] = None
    editingTime: Optional[float] = None


class MatchCounts101Dto(BaseModel):
    match100: Optional[CountsDto] = None
    match95: Optional[CountsDto] = None
    match85: Optional[CountsDto] = None
    match75: Optional[CountsDto] = None
    match50: Optional[CountsDto] = None
    match0: Optional[CountsDto] = None
    match101: Optional[CountsDto] = None


class MatchCountsDto(BaseModel):
    match100: Optional[CountsDto] = None
    match95: Optional[CountsDto] = None
    match85: Optional[CountsDto] = None
    match75: Optional[CountsDto] = None
    match50: Optional[CountsDto] = None
    match0: Optional[CountsDto] = None


class MatchCountsNTDtoV1(BaseModel):
    match100: Optional[CountsDto] = None
    match99: Optional[CountsDto] = None


class NetRateSchemeReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None


class AnalyseRecalculateRequestDto(BaseModel):
    analyses: List[IdReference] = Field(..., max_items=100, min_items=1)
    callbackUrl: Optional[str] = None


class CleanupTask(BaseModel):
    pass


class InputStream(BaseModel):
    pass


class InputStreamLength(BaseModel):
    stream: Optional[InputStream] = None
    length: Optional[int] = None
    name: Optional[str] = None
    characterEncoding: Optional[str] = None
    extension: Optional[str] = None
    cleanupTask: Optional[CleanupTask] = None


class Type(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    Compare = "Compare"


class CreateAnalyseListAsyncDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    type: Optional[Type] = Field(None, description="default: PreAnalyse")
    includeFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    separateFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    includeConfirmedSegments: Optional[bool] = Field(None, description="Default: true")
    includeNumbers: Optional[bool] = Field(None, description="Default: true")
    includeLockedSegments: Optional[bool] = Field(None, description="Default: true")
    countSourceUnits: Optional[bool] = Field(None, description="Default: true")
    includeTransMemory: Optional[bool] = Field(
        None, description="Default: true. Works only for type=PreAnalyse."
    )
    includeNonTranslatables: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PreAnalyse."
    )
    includeMachineTranslationMatches: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PreAnalyse."
    )
    transMemoryPostEditing: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PostAnalyse."
    )
    nonTranslatablePostEditing: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PostAnalyse."
    )
    machineTranslatePostEditing: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PostAnalyse."
    )
    name: Optional[constr(min_length=0, max_length=255)] = None
    netRateScheme: Optional[IdReference] = None
    compareWorkflowLevel: Optional[conint(ge=1, le=15)] = Field(
        None, description="Required for type=Compare"
    )
    useProjectAnalysisSettings: Optional[bool] = Field(
        None,
        description="Default: false. Use default project settings. Will be overwritten with setting sent\n        in the API call.",
    )
    callbackUrl: Optional[str] = None


class BulkDeleteAnalyseDto(BaseModel):
    analyses: List[IdReference] = Field(..., max_items=100, min_items=1)
    purge: Optional[bool] = Field(None, description="Default: false")


class ConcurrentRequestsDto(BaseModel):
    limit: Optional[int] = Field(
        None,
        description="Max number of allowed concurrent request, null value means no limit",
    )
    count: Optional[int] = Field(
        None, description="Current count of running concurrent requests"
    )


class LoginResponseDto(BaseModel):
    user: Optional[UserReference] = None
    token: Optional[str] = None
    expires: Optional[datetime] = None
    lastInvalidateAllSessionsPerformed: Optional[datetime] = None


class LoginDto(BaseModel):
    userName: str
    password: str
    code: Optional[str] = Field(
        None, description="Required only for 2-factor authentication"
    )


class LoginToSessionResponseDto(BaseModel):
    user: Optional[UserReference] = None
    cookie: Optional[str] = None
    csrfToken: Optional[str] = None


class LoginToSessionDto(BaseModel):
    userName: str
    password: str
    rememberMe: Optional[bool] = None


class LoginOtherDto(BaseModel):
    userName: str


class EditionDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None


class FeaturesDto(BaseModel):
    icuEnabled: Optional[bool] = None
    rejectJobs: Optional[bool] = None
    qaHighlightsEnabled: Optional[bool] = None
    lqaBulkCommentsCreation: Optional[bool] = None
    mentionsAndNotificationsEnabled: Optional[bool] = None
    mtForTMAbove100Enabled: Optional[bool] = None


class OrganizationReference(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None


class LoginWithGoogleDto(BaseModel):
    idToken: str


class LoginWithAppleDto(BaseModel):
    codeOrRefreshToken: str


class AppleTokenResponseDto(BaseModel):
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    expires_in: Optional[str] = None
    refresh_token: Optional[str] = None
    id_token: Optional[str] = None


class Status(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ProviderReference(BaseModel):
    type: str
    id: Optional[str] = None
    uid: Optional[str] = None


class USER(ProviderReference):
    userName: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    active: Optional[bool] = None


class VENDOR(ProviderReference):
    name: Optional[str] = None
    defaultProjectOwnerId: Optional[int] = None


class WorkflowStepReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None
    order: Optional[int] = None
    lqaEnabled: Optional[bool] = None


class State(Enum):
    Miss = "Miss"
    Diff = "Diff"


class ComparedSegmentDto(BaseModel):
    uid: Optional[str] = None
    state: Optional[State] = None


class ComparedSegmentsDto(BaseModel):
    segments: Optional[List[ComparedSegmentDto]] = None


class BusinessUnitDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[UserReference] = None


class BusinessUnitEditDto(BaseModel):
    name: constr(min_length=0, max_length=255)


class PageDtoBusinessUnitDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[BusinessUnitDto]] = None


class ClientReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None


class PriceListReference(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    uid: Optional[str] = None


class ClientEditDto(BaseModel):
    name: constr(min_length=0, max_length=255)
    externalId: Optional[constr(min_length=0, max_length=255)] = None
    note: Optional[constr(min_length=0, max_length=4096)] = None
    displayNoteInProject: Optional[bool] = Field(None, description="Default: false")
    priceList: Optional[IdReference] = None
    netRateScheme: Optional[IdReference] = None


class Type1(Enum):
    DROPBOX = "DROPBOX"
    GOOGLE = "GOOGLE"
    FTP = "FTP"
    WORDPRESS = "WORDPRESS"
    GITHUB = "GITHUB"
    SFTP = "SFTP"
    DRUPAL = "DRUPAL"
    BOX = "BOX"
    GIT = "GIT"
    ZENDESK = "ZENDESK"
    ONEDRIVE = "ONEDRIVE"
    GITLAB = "GITLAB"
    MARKETO = "MARKETO"
    HUBSPOT = "HUBSPOT"
    HELPSCOUT = "HELPSCOUT"
    SALESFORCE = "SALESFORCE"
    BITBUCKET = "BITBUCKET"
    BITBUCKETSERVER = "BITBUCKETSERVER"
    BRAZE = "BRAZE"
    SHAREPOINT = "SHAREPOINT"
    AZURE = "AZURE"
    SITECORE = "SITECORE"
    KENTICO = "KENTICO"
    KENTICO_KONTENT = "KENTICO_KONTENT"
    MAGENTO = "MAGENTO"
    CONTENTFULENTRYLEVEL = "CONTENTFULENTRYLEVEL"
    CONTENTFUL = "CONTENTFUL"
    CONTENTSTACK = "CONTENTSTACK"
    JOOMLA = "JOOMLA"
    CONFLUENCE = "CONFLUENCE"
    TYPO3 = "TYPO3"
    AEM_PLUGIN = "AEM_PLUGIN"
    DRUPAL_PLUGIN = "DRUPAL_PLUGIN"
    AMAZON_S3 = "AMAZON_S3"
    PARDOT = "PARDOT"
    PHRASE = "PHRASE"


class NameDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class ConnectorCreateResponseDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    created: Optional[datetime] = None
    status: Optional[str] = None
    linkedAccount: Optional[str] = None


class AbstractConnectorDto(BaseModel):
    name: constr(min_length=0, max_length=255) = Field(
        ..., description="Name of the connector"
    )
    type: str = Field(..., description="Connector type")


class AdobeExperienceManager(AbstractConnectorDto):
    urlRewriteFind: Optional[str] = None
    urlRewriteReplace: Optional[str] = None
    host: str


class AmazonS3(AbstractConnectorDto):
    apiKey: str
    apiSecret: str


class BitbucketServer(AbstractConnectorDto):
    host: str
    commitMessage: Optional[str] = None
    token: str


class Contentstack(AbstractConnectorDto):
    authType: str
    region: Optional[str] = None
    nonLocalizableBlocksUids: Optional[str] = None
    targetLangsFieldId: Optional[str] = None
    apiKey: str
    sourceLang: Optional[str] = None
    translateUrls: Optional[bool] = Field(None, description="Default false")
    translateTags: Optional[bool] = Field(None, description="Default false")
    managementToken: Optional[str] = None
    password: Optional[str] = None
    userName: Optional[str] = None
    stackWFObserved: Optional[str] = None
    stackWFUponImport: Optional[str] = None
    stackWFExportSource: Optional[str] = None
    stackWFExportTranslate: Optional[str] = None


class Ftp(AbstractConnectorDto):
    userName: str
    password: str
    host: str
    port: int
    encryption: Optional[str] = Field(None, description="Default TLS_IF_AVAILABLE")


class Git(AbstractConnectorDto):
    userName: str
    password: str
    host: str
    commitMessage: Optional[str] = None
    sshKeyName: Optional[str] = None
    sshKey: Optional[str] = None
    sshPassPhrase: Optional[str] = None


class GitLab(AbstractConnectorDto):
    commitMessage: Optional[str] = None
    host: str
    token: str


class Joomla(AbstractConnectorDto):
    host: str
    token: str


class Kentico(AbstractConnectorDto):
    userName: str
    password: str
    host: str
    sourceLang: Optional[str] = None


class Magento(AbstractConnectorDto):
    host: str
    token: str


class MarketoSegmentMappingDto(BaseModel):
    segmentId: Optional[int] = None
    locale: Optional[str] = None
    source: Optional[bool] = None


class MarketoSegmentationMappingDto(BaseModel):
    segmentationId: Optional[int] = None
    segmentsMapping: Optional[List[MarketoSegmentMappingDto]] = None


class MicrosoftAzure(AbstractConnectorDto):
    connectionString: str = Field(..., description="Microsoft azure connection string")


class Sftp(AbstractConnectorDto):
    host: str
    port: int
    userName: str
    password: str
    sshKeyName: Optional[str] = None
    sshKey: Optional[str] = None
    sshPassPhrase: Optional[str] = None


class Sitecore(AbstractConnectorDto):
    userName: str
    password: str
    host: str
    sitecoreDatabase: str
    sourceLang: Optional[str] = None


class Typo3(AbstractConnectorDto):
    host: str
    sourceLang: Optional[str] = None
    token: str


class VariableDto(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None


class Wordpress(AbstractConnectorDto):
    basicAuthUserName: str
    basicAuthPassword: str
    host: str
    token: str = Field(..., description="Memsource plugin token")


class ConnectorErrorDetailDto(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None
    messageCode: Optional[str] = None
    args: Optional[Dict[str, Dict[str, Any]]] = None
    skipPrefix: Optional[bool] = None


class ConnectorErrorsDto(BaseModel):
    errors: Optional[List[ConnectorErrorDetailDto]] = None


class UploadResultDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    folder: Optional[str] = None
    encodedName: Optional[str] = None
    size: Optional[int] = None
    error: Optional[str] = None
    asyncTaskId: Optional[str] = None
    errors: Optional[ConnectorErrorsDto] = None


class ErrorDto(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None


class FileDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    encodedName: Optional[str] = None
    contentType: Optional[str] = None
    note: Optional[str] = None
    size: Optional[int] = None
    directory: Optional[bool] = None
    lastModified: Optional[datetime] = None
    selected: Optional[bool] = None
    error: Optional[ErrorDto] = None
    escapedName: Optional[str] = None


class FileListDto(BaseModel):
    files: Optional[List[FileDto]] = None
    currentFolder: Optional[str] = None
    encodedCurrentFolder: Optional[str] = None
    rootFolder: Optional[bool] = None
    lastChangedFiles: Optional[List[FileDto]] = None


class Type2(Enum):
    PROJECT_OWNER = "PROJECT_OWNER"
    JOB_OWNER = "JOB_OWNER"
    PROVIDER = "PROVIDER"
    GUEST = "GUEST"


class OrganizationType(Enum):
    VENDOR = "VENDOR"
    BUYER = "BUYER"


class Repeated(Enum):
    REPEATED = "REPEATED"
    NOT_REPEATED = "NOT_REPEATED"


class LQAReference(BaseModel):
    errorCategoryId: conint(ge=1)
    severityId: conint(ge=1)
    user: Optional[IdReference] = None
    repeated: Optional[Repeated] = Field(None, description="Default: `NOT_REPEATED`")


class Interaction(Enum):
    PLAIN_CONVERSATION_THREAD_REPLY = "PLAIN_CONVERSATION_THREAD_REPLY"
    PLAIN_CONVERSATION_MENTION = "PLAIN_CONVERSATION_MENTION"
    PLAIN_CONVERSATION_MENTION_THREAD_REPLY = "PLAIN_CONVERSATION_MENTION_THREAD_REPLY"
    LQA_CONVERSATION_THREAD_REPLY = "LQA_CONVERSATION_THREAD_REPLY"
    LQA_CONVERSATION_MENTION = "LQA_CONVERSATION_MENTION"
    LQA_CONVERSATION_MENTION_THREAD_REPLY = "LQA_CONVERSATION_MENTION_THREAD_REPLY"
    LQA_FINISHED = "LQA_FINISHED"


class Role1(Enum):
    SYS_ADMIN = "SYS_ADMIN"
    SYS_ADMIN_READ = "SYS_ADMIN_READ"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LINGUIST = "LINGUIST"
    GUEST = "GUEST"
    SUBMITTER = "SUBMITTER"


class Role2(Enum):
    PARENT = "PARENT"


class ReferenceCorrelation(BaseModel):
    uid: Optional[str] = None
    role: Optional[Role2] = None


class Name(Enum):
    resolved = "resolved"
    unresolved = "unresolved"


class WorkflowStepReferenceV2(BaseModel):
    name: Optional[str] = None
    uid: Optional[str] = None
    id: Optional[str] = None
    order: Optional[int] = None
    lqaEnabled: Optional[bool] = None


class FindConversationsDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    since: Optional[str] = None
    includeDeleted: Optional[bool] = Field(None, description="Default: false")


class CostCenterDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[UserReference] = None


class PageDtoCostCenterDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[CostCenterDto]] = None


class CostCenterEditDto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None


class AndroidSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None


class AsciidocSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None
    htmlInPassthrough: Optional[bool] = Field(None, description="Default: `false`")
    nontranslatableMonospaceCustomStylesRegexp: Optional[str] = None
    extractCustomDocumentAttributeNameRegexp: Optional[str] = Field(
        None, description="Default: `.*`"
    )
    extractBtnMenuLabels: Optional[bool] = Field(None, description="Default: `false`")


class DelimiterType(Enum):
    TAB = "TAB"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    OTHER = "OTHER"


class CsvSettingsDto(BaseModel):
    delimiter: Optional[str] = Field(None, description="Default: ,")
    delimiterType: Optional[DelimiterType] = Field(None, description="Default: COMMA")
    htmlSubFilter: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None
    importColumns: Optional[str] = None
    contextNoteColumns: Optional[str] = None
    contextKeyColumn: Optional[str] = None
    maxLenColumn: Optional[str] = None
    importRows: Optional[str] = None


class DitaSettingsDto(BaseModel):
    includeTags: Optional[str] = None
    excludeTags: Optional[str] = None
    inlineTags: Optional[str] = None
    inlineTagsNonTranslatable: Optional[str] = None
    tagRegexp: Optional[str] = None


class DocBookSettingsDto(BaseModel):
    includeTags: Optional[str] = None
    excludeTags: Optional[str] = None
    inlineTags: Optional[str] = None
    inlineTagsNonTranslatable: Optional[str] = None
    tagRegexp: Optional[str] = None


class DocSettingsDto(BaseModel):
    comments: Optional[bool] = Field(None, description="Default: false")
    index: Optional[bool] = Field(None, description="Default: true")
    other: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None
    hyperlinkTarget: Optional[bool] = Field(None, description="Default: false")
    joinSimilarRuns: Optional[bool] = Field(None, description="Default: false")
    targetFont: Optional[str] = None
    properties: Optional[bool] = Field(None, description="Default: false")
    hidden: Optional[bool] = Field(None, description="Default: false")
    headerFooter: Optional[bool] = Field(None, description="Default: true")


class HtmlSettingsDto(BaseModel):
    breakTagCreatesSegment: Optional[bool] = Field(None, description="Default: true")
    unknownTagCreatesTag: Optional[bool] = Field(None, description="Default: true")
    preserveWhitespace: Optional[bool] = Field(None, description="Default: false")
    importComments: Optional[bool] = Field(None, description="Default: true")
    excludeElements: Optional[str] = Field(
        None, description='Example: "script,blockquote"'
    )
    tagRegexp: Optional[str] = None
    charEntitiesToTags: Optional[str] = None
    translateMetaTagRegexp: Optional[str] = None
    importDefaultMetaTags: Optional[bool] = Field(None, description="Default: true")
    translatableAttributes: Optional[str] = None
    importDefaultAttributes: Optional[bool] = Field(None, description="Default: true")
    nonTranslatableInlineElements: Optional[str] = Field(
        None, description='Example: "code"'
    )
    translatableInlineElements: Optional[str] = Field(
        None, description='Example: "span"'
    )
    updateLang: Optional[bool] = Field(None, description="Default: false")
    escapeDisabled: Optional[bool] = Field(None, description="Default: `false`")


class IdmlSettingsDto(BaseModel):
    extractNotes: Optional[bool] = Field(None, description="Default: false")
    simplifyCodes: Optional[bool] = Field(None, description="Default: true")
    extractMasterSpreads: Optional[bool] = Field(None, description="Default: true")
    extractLockedLayers: Optional[bool] = Field(None, description="Default: true")
    extractInvisibleLayers: Optional[bool] = Field(None, description="Default: false")
    extractHiddenConditionalText: Optional[bool] = Field(
        None, description="Default: false"
    )
    extractHyperlinks: Optional[bool] = Field(None, description="Default: false")
    keepKerning: Optional[bool] = Field(None, description="Default: false")
    keepTracking: Optional[bool] = Field(None, description="Default: false")
    targetFont: Optional[str] = None
    replaceFont: Optional[bool] = Field(None, description="Default: true")
    removeXmlElements: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None
    extractCrossReferenceFormats: Optional[bool] = Field(
        None, description="Default: true"
    )
    extractVariables: Optional[bool] = Field(None, description="Default: true")


class JsonSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None
    htmlSubFilter: Optional[bool] = Field(None, description="Default: true")
    icuSubFilter: Optional[bool] = Field(None, description="Default: false")
    excludeKeyRegexp: Optional[str] = None
    includeKeyRegexp: Optional[str] = None
    contextNotePath: Optional[str] = None
    maxLenPath: Optional[str] = None
    contextKeyPath: Optional[str] = None


class MacSettingsDto(BaseModel):
    htmlSubfilter: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None


class Flavor(Enum):
    PLAIN = "PLAIN"
    PHP = "PHP"
    GITHUB = "GITHUB"


class MdSettingsDto(BaseModel):
    hardLineBreaksSegments: Optional[bool] = Field(None, description="Default: true")
    preserveWhiteSpaces: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None
    customElements: Optional[str] = None
    ignoredBlockPrefixes: Optional[str] = None
    flavor: Optional[Flavor] = Field(None, description="Default: PLAIN")
    processJekyllFrontMatter: Optional[bool] = Field(None, description="Default: false")
    extractCodeBlocks: Optional[bool] = Field(None, description="Default: true")
    notEscapedCharacters: Optional[str] = None
    excludeCodeElements: Optional[bool] = Field(None, description="Default: false")


class Type3(Enum):
    CLIENT = "CLIENT"
    DOMAIN = "DOMAIN"
    SUBDOMAIN = "SUBDOMAIN"
    FILENAME = "FILENAME"


class MetadataField(BaseModel):
    type: Optional[Type3] = None


class MetadataPrioritySettingsDto(BaseModel):
    prioritizedFields: List[MetadataField]


class MifSettingsDto(BaseModel):
    extractBodyPages: Optional[bool] = Field(None, description="Default: true")
    extractReferencePages: Optional[bool] = Field(None, description="Default: false")
    extractMasterPages: Optional[bool] = Field(None, description="Default: true")
    extractHiddenPages: Optional[bool] = Field(None, description="Default: false")
    extractVariables: Optional[bool] = Field(None, description="Default: false")
    extractIndexMarkers: Optional[bool] = Field(None, description="Default: true")
    extractLinks: Optional[bool] = Field(None, description="Default: false")
    extractXRefDef: Optional[bool] = Field(None, description="Default: false")
    extractPgfNumFormat: Optional[bool] = Field(None, description="Default: true")
    extractCustomReferencePages: Optional[bool] = Field(
        None, description="Default: true"
    )
    extractDefaultReferencePages: Optional[bool] = Field(
        None, description="Default: false"
    )
    extractUsedVariables: Optional[bool] = Field(None, description="Default: true")
    extractHiddenCondText: Optional[bool] = Field(None, description="Default: false")
    extractUsedXRefDef: Optional[bool] = Field(None, description="Default: true")
    extractUsedPgfNumFormat: Optional[bool] = Field(None, description="Default: true")
    tagRegexp: Optional[str] = None


class DelimiterType1(Enum):
    TAB = "TAB"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    OTHER = "OTHER"


class NonEmptySegmentAction(Enum):
    NONE = "NONE"
    CONFIRM = "CONFIRM"
    LOCK = "LOCK"
    CONFIRM_LOCK = "CONFIRM_LOCK"


class MultilingualCsvSettingsDto(BaseModel):
    sourceColumns: Optional[str] = None
    targetColumns: Optional[str] = None
    contextNoteColumns: Optional[str] = None
    contextKeyColumns: Optional[str] = None
    tagRegexp: Optional[str] = None
    htmlSubFilter: Optional[bool] = Field(None, description="Default: false")
    segmentation: Optional[bool] = Field(None, description="Default: true")
    delimiter: Optional[constr(min_length=0, max_length=255)] = Field(
        None, description="Default: ,"
    )
    delimiterType: Optional[DelimiterType1] = Field(None, description="Default: COMMA")
    importRows: Optional[str] = None
    maxLenColumns: Optional[str] = None
    allTargetColumns: Optional[Dict[str, str]] = Field(
        None, description='Format: "language":"column"; example: {"en": "A", "sk": "B"}'
    )
    nonEmptySegmentAction: Optional[NonEmptySegmentAction] = None
    saveConfirmedSegmentsToTm: Optional[bool] = None


class NonEmptySegmentAction1(Enum):
    NONE = "NONE"
    CONFIRM = "CONFIRM"
    LOCK = "LOCK"
    CONFIRM_LOCK = "CONFIRM_LOCK"


class MultilingualXlsSettingsDto(BaseModel):
    sourceColumn: Optional[str] = None
    targetColumns: Optional[Dict[str, str]] = Field(
        None, description='Format: "language":"column"; example: {"en": "A", "sk": "B"}'
    )
    contextNoteColumn: Optional[str] = None
    contextKeyColumn: Optional[str] = None
    tagRegexp: Optional[str] = None
    htmlSubFilter: Optional[bool] = Field(None, description="Default: false")
    segmentation: Optional[bool] = Field(None, description="Default: true")
    importRows: Optional[str] = None
    maxLenColumn: Optional[str] = None
    nonEmptySegmentAction: Optional[NonEmptySegmentAction1] = None
    saveConfirmedSegmentsToTm: Optional[bool] = None


class NonEmptySegmentAction2(Enum):
    NONE = "NONE"
    CONFIRM = "CONFIRM"
    LOCK = "LOCK"
    CONFIRM_LOCK = "CONFIRM_LOCK"


class MultilingualXmlSettingsDto(BaseModel):
    translatableElementsXPath: Optional[str] = None
    sourceElementsXPath: Optional[str] = None
    targetElementsXPaths: Optional[Dict[str, str]] = Field(
        None,
        description='\'Format: "language":"xpath";\n            example = \'{"en": "tuv[@lang=\'en\']/seg", "sk": "tuv[@lang=\'sk\']/seg"}',
    )
    inlineElementsNonTranslatableXPath: Optional[str] = None
    tagRegexp: Optional[str] = None
    segmentation: Optional[bool] = Field(None, description="Default: `true`")
    htmlSubFilter: Optional[bool] = Field(None, description="Default: `false`")
    contextKeyXPath: Optional[str] = None
    contextNoteXPath: Optional[str] = None
    maxLenXPath: Optional[str] = None
    preserveWhitespace: Optional[bool] = Field(None, description="Default: `false`")
    preserveCharEntities: Optional[str] = None
    xslUrl: Optional[str] = None
    xslFile: Optional[str] = Field(
        None, description="UID of uploaded XSL file, overrides xslUrl"
    )
    nonEmptySegmentAction: Optional[NonEmptySegmentAction2] = None
    saveConfirmedSegmentsToTm: Optional[bool] = None


class Filter(Enum):
    TRANS_PDF = "TRANS_PDF"
    DEFAULT = "DEFAULT"


class PdfSettingsDto(BaseModel):
    filter: Optional[Filter] = Field(None, description="Default: TRANS_PDF")


class PhpSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None
    htmlSubFilter: Optional[bool] = Field(None, description="Default: false")


class ImportSetSegmentConfirmedWhen(Enum):
    FUZZY = "FUZZY"
    NONFUZZY = "NONFUZZY"


class ImportSetSegmentLockedWhen(Enum):
    FUZZY = "FUZZY"
    NONFUZZY = "NONFUZZY"


class ExportConfirmedLocked(Enum):
    FUZZY = "FUZZY"
    NONFUZZY = "NONFUZZY"


class ExportConfirmedNotLocked(Enum):
    FUZZY = "FUZZY"
    NONFUZZY = "NONFUZZY"


class ExportNotConfirmedLocked(Enum):
    FUZZY = "FUZZY"
    NONFUZZY = "NONFUZZY"


class ExportNotConfirmedNotLocked(Enum):
    FUZZY = "FUZZY"
    NONFUZZY = "NONFUZZY"


class PoSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None
    exportMultiline: Optional[bool] = Field(None, description="Default: true")
    htmlSubFilter: Optional[bool] = Field(None, description="Default: false")
    segment: Optional[bool] = Field(None, description="Default: false")
    markupSubFilterTranslatable: Optional[str] = None
    markupSubFilterNonTranslatable: Optional[str] = None
    saveConfirmedSegments: Optional[bool] = None
    importSetSegmentConfirmedWhen: Optional[ImportSetSegmentConfirmedWhen] = None
    importSetSegmentLockedWhen: Optional[ImportSetSegmentLockedWhen] = None
    exportConfirmedLocked: Optional[ExportConfirmedLocked] = None
    exportConfirmedNotLocked: Optional[ExportConfirmedNotLocked] = None
    exportNotConfirmedLocked: Optional[ExportNotConfirmedLocked] = None
    exportNotConfirmedNotLocked: Optional[ExportNotConfirmedNotLocked] = None


class PptSettingsDto(BaseModel):
    hiddenSlides: Optional[bool] = Field(None, description="Default: false")
    other: Optional[bool] = Field(None, description="Default: false")
    notes: Optional[bool] = Field(None, description="Default: false")
    masterSlides: Optional[bool] = Field(None, description="Default: false")


class PropertiesSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None


class PsdSettingsDto(BaseModel):
    extractHiddenLayers: Optional[bool] = Field(None, description="Default: true")
    extractLockedLayers: Optional[bool] = Field(None, description="Default: true")
    tagRegexp: Optional[str] = None


class QuarkTagSettingsDto(BaseModel):
    removeKerningTrackingTags: Optional[bool] = Field(
        None, description="Default: false"
    )
    tagRegexp: Optional[str] = None


class ResxSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None
    htmlSubFilter: Optional[bool] = None


class SdlXlfSettingsDto(BaseModel):
    icuSubFilter: Optional[bool] = Field(None, description="Default: false")
    skipImportRules: Optional[str] = Field(None, description="Default: translate=no")
    importAsConfirmedRules: Optional[str] = None
    importAsLockedRules: Optional[str] = Field(None, description="Default: locked=true")
    exportAttrsWhenConfirmedAndLocked: Optional[str] = Field(
        None, description="Default: locked=true"
    )
    exportAttrsWhenConfirmedAndNotLocked: Optional[str] = None
    exportAttrsWhenNotConfirmedAndLocked: Optional[str] = Field(
        None, description="Default: locked=true"
    )
    exportAttrsWhenNotConfirmedAndNotLocked: Optional[str] = None
    saveConfirmedSegments: Optional[bool] = Field(None, description="Default: true")
    tagRegexp: Optional[str] = None


class SegRuleReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    language: Optional[str] = None
    name: Optional[str] = None
    filename: Optional[str] = None
    primary: Optional[bool] = None


class ContextType(Enum):
    AUTO = "AUTO"
    PREV_AND_NEXT_SEGMENT = "PREV_AND_NEXT_SEGMENT"
    SEGMENT_KEY = "SEGMENT_KEY"
    NO_CONTEXT = "NO_CONTEXT"


class TMMatchSettingsDto(BaseModel):
    contextType: Optional[ContextType] = Field(
        None, description="Default: PREV_AND_NEXT_SEGMENT"
    )
    prevOrNextSegment: Optional[bool] = Field(None, description="Default: false")
    penalizeMultiContextMatch: Optional[bool] = Field(
        None, description="Default: false"
    )
    ignoreTagMetadata: Optional[bool] = Field(None, description="Default: true")
    metadataPriority: Optional[MetadataPrioritySettingsDto] = None


class TtxSettingsDto(BaseModel):
    saveConfirmedSegments: Optional[bool] = Field(None, description="Default: true")


class TxtSettingsDto(BaseModel):
    tagRegexp: Optional[str] = None
    translatableTextRegexp: Optional[str] = None
    contextKey: Optional[str] = None
    regexpCapturingGroups: Optional[bool] = Field(None, description="Default: false")


class Xlf2SettingsDto(BaseModel):
    icuSubFilter: Optional[bool] = Field(None, description="Default: false")
    importNotes: Optional[bool] = Field(None, description="Default: true")
    saveConfirmedSegments: Optional[bool] = Field(None, description="Default: true")
    segmentation: Optional[bool] = Field(None, description="Default: true")
    lineBreakTags: Optional[bool] = Field(None, description="Default: false")
    preserveWhitespace: Optional[bool] = Field(None, description="Default: true")
    copySourceToTargetIfNotImported: Optional[bool] = Field(
        None, description="Default: true"
    )
    respectTranslateAttr: Optional[bool] = Field(None, description="Default: true")
    skipImportRules: Optional[str] = None
    importAsConfirmedRules: Optional[str] = Field(
        None, description="Default: state=final"
    )
    importAsLockedRules: Optional[str] = None
    exportAttrsWhenConfirmedAndLocked: Optional[str] = Field(
        None, description="Default: state=final"
    )
    exportAttrsWhenConfirmedAndNotLocked: Optional[str] = Field(
        None, description="Default: state=final"
    )
    exportAttrsWhenNotConfirmedAndLocked: Optional[str] = None
    exportAttrsWhenNotConfirmedAndNotLocked: Optional[str] = None
    contextKeyXPath: Optional[str] = None
    preserveCharEntities: Optional[str] = None
    xslUrl: Optional[str] = None
    xslFile: Optional[str] = Field(
        None, description="UID of uploaded XSL file, overrides xslUrl"
    )
    tagRegexp: Optional[str] = None


class XlfSettingsDto(BaseModel):
    icuSubFilter: Optional[bool] = Field(None, description="Default: false")
    importNotes: Optional[bool] = Field(None, description="Default: true")
    segmentation: Optional[bool] = Field(None, description="Default: true")
    skipImportRules: Optional[str] = Field(
        None,
        description="Default: translate=no; examples: translate=no;approved=no;state=needs-adaptation",
    )
    importAsConfirmedRules: Optional[str] = Field(
        None, description="Multiple rules must be separated by semicolon"
    )
    importAsLockedRules: Optional[str] = None
    exportAttrsWhenConfirmedAndLocked: Optional[str] = None
    exportAttrsWhenConfirmedAndNotLocked: Optional[str] = None
    exportAttrsWhenNotConfirmedAndLocked: Optional[str] = None
    exportAttrsWhenNotConfirmedAndNotLocked: Optional[str] = None
    saveConfirmedSegments: Optional[bool] = Field(None, description="Default: true")
    lineBreakTags: Optional[bool] = Field(None, description="Default: false")
    preserveWhitespace: Optional[bool] = Field(None, description="Default: true")
    contextType: Optional[str] = None
    preserveCharEntities: Optional[str] = None
    copySourceToTargetIfNotImported: Optional[bool] = Field(
        None, description="Default: true"
    )
    importXPath: Optional[str] = None
    importAsConfirmedXPath: Optional[str] = None
    importAsLockedXPath: Optional[str] = None
    xslUrl: Optional[str] = None
    xslFile: Optional[str] = Field(
        None, description="UID of uploaded XSL file, overrides xslUrl"
    )
    tagRegexp: Optional[str] = None


class CellFlow(Enum):
    DownRight = "DownRight"
    RightDown = "RightDown"
    DownLeft = "DownLeft"
    LeftDown = "LeftDown"


class XlsSettingsDto(BaseModel):
    sheetNames: Optional[bool] = Field(None, description="Default: false")
    hidden: Optional[bool] = Field(None, description="Default: false")
    comments: Optional[bool] = Field(None, description="Default: false")
    other: Optional[bool] = Field(None, description="Default: false")
    cellFlow: Optional[CellFlow] = Field(None, description="Default: DownRight")
    htmlSubfilter: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None
    specifiedColumns: Optional[str] = None


class RulesFormat(Enum):
    PLAIN = "PLAIN"
    XPATH = "XPATH"


class XmlSettingsDto(BaseModel):
    rulesFormat: Optional[RulesFormat] = Field(None, description='Default: `"PLAIN"`')
    includeElementsPlain: Optional[str] = Field(
        None, description='Default: `"*"`, example: `"para,heading"`'
    )
    excludeElementsPlain: Optional[str] = Field(
        None, description='Example: `"script,par"`'
    )
    includeAttributesPlain: Optional[str] = Field(
        None, description='Example: `"title"`'
    )
    excludeAttributesPlain: Optional[str] = Field(
        None, description='Example: `"lang,href"`'
    )
    inlineElementsNonTranslatablePlain: Optional[str] = Field(
        None, description='Example: `"tt,b"`'
    )
    inlineElementsPlain: Optional[str] = None
    inlineElementsAutoPlain: Optional[bool] = Field(
        None, description="Default: `false`"
    )
    htmlSubfilterElementsPlain: Optional[str] = Field(
        None, description='Example: `"tt,b"`'
    )
    entities: Optional[bool] = Field(None, description="Default: `false`")
    lockElementsPlain: Optional[str] = None
    lockAttributesPlain: Optional[str] = None
    includeXPath: Optional[str] = None
    inlineElementsXpath: Optional[str] = None
    inlineElementsNonTranslatableXPath: Optional[str] = None
    inlineElementsAutoXPath: Optional[bool] = Field(
        None, description="Default: `false`"
    )
    htmlSubfilterElementsXpath: Optional[str] = None
    lockXPath: Optional[str] = None
    segmentation: Optional[bool] = Field(None, description="Default: `true`")
    tagRegexp: Optional[str] = None
    contextNoteXpath: Optional[str] = None
    maxLenXPath: Optional[str] = None
    preserveWhitespaceXPath: Optional[str] = None
    preserveCharEntities: Optional[str] = None
    contextKeyXPath: Optional[str] = None
    xslUrl: Optional[str] = None
    xslFile: Optional[str] = Field(
        None, description="UID of uploaded XSL file, overrides `xslUrl`"
    )
    importComments: Optional[bool] = Field(None, description="Default: `true`")


class LocaleFormat(Enum):
    MEMSOURCE = "MEMSOURCE"
    RFC_5646 = "RFC_5646"
    ANDROID_QUALIFIER = "ANDROID_QUALIFIER"
    ANDROID_QUALIFIER_BCP = "ANDROID_QUALIFIER_BCP"


class YamlSettingsDto(BaseModel):
    htmlSubFilter: Optional[bool] = Field(None, description="Default: false")
    tagRegexp: Optional[str] = None
    includeKeyRegexp: Optional[str] = None
    excludeValueRegexp: Optional[str] = None
    contextPath: Optional[str] = None
    contextKeyPath: Optional[str] = None
    markdownSubfilter: Optional[bool] = Field(None, description="Default: false")
    updateRootElementLang: Optional[bool] = Field(None, description="Default: false")
    localeFormat: Optional[LocaleFormat] = None
    indentEmptyLinesInString: Optional[bool] = Field(None, description="Default: true")


class Type4(Enum):
    html = "html"
    json = "json"
    xml = "xml"
    multiling_xml = "multiling_xml"
    txt = "txt"


class FileFormat(Enum):
    doc = "doc"
    ppt = "ppt"
    xls = "xls"
    xlf = "xlf"
    xlf2 = "xlf2"
    sdlxlif = "sdlxlif"
    ttx = "ttx"
    html = "html"
    xml = "xml"
    mif = "mif"
    tmx = "tmx"
    idml = "idml"
    dita = "dita"
    json = "json"
    po = "po"
    ts = "ts"
    icml = "icml"
    yaml = "yaml"
    properties = "properties"
    csv = "csv"
    android_string = "android_string"
    desktop_entry = "desktop_entry"
    mac_strings = "mac_strings"
    pdf = "pdf"
    windows_rc = "windows_rc"
    xml_properties = "xml_properties"
    joomla_ini = "joomla_ini"
    magento_csv = "magento_csv"
    dtd = "dtd"
    mozilla_properties = "mozilla_properties"
    plist = "plist"
    plain_text = "plain_text"
    srt = "srt"
    sub = "sub"
    sbv = "sbv"
    wiki = "wiki"
    resx = "resx"
    resjson = "resjson"
    chrome_json = "chrome_json"
    epub = "epub"
    svg = "svg"
    docbook = "docbook"
    wpxliff = "wpxliff"
    multiling_xml = "multiling_xml"
    multiling_xls = "multiling_xls"
    mqxliff = "mqxliff"
    php = "php"
    psd = "psd"
    tag = "tag"
    md = "md"
    vtt = "vtt"


class FileImportSettingsCreateDto(BaseModel):
    inputCharset: Optional[str] = None
    outputCharset: Optional[str] = None
    zipCharset: Optional[str] = None
    fileFormat: Optional[FileFormat] = Field(None, description="default: auto-detect")
    autodetectMultilingualFiles: Optional[bool] = Field(
        None,
        description="Try to use multilingual variants for auto-detected CSV and Excel files. Default: true",
    )
    targetLength: Optional[bool] = Field(None, description="Default: false")
    targetLengthMax: Optional[int] = Field(None, description="default: 1000")
    targetLengthPercent: Optional[bool] = Field(None, description="Default: false")
    targetLengthPercentValue: Optional[float] = Field(None, description="default: 130")
    segmentationRuleId: Optional[int] = None
    targetSegmentationRuleId: Optional[int] = None
    android: Optional[AndroidSettingsDto] = None
    csv: Optional[CsvSettingsDto] = None
    dita: Optional[DitaSettingsDto] = None
    docBook: Optional[DocBookSettingsDto] = None
    doc: Optional[DocSettingsDto] = None
    html: Optional[HtmlSettingsDto] = None
    idml: Optional[IdmlSettingsDto] = None
    json_: Optional[JsonSettingsDto] = Field(None, alias="json")
    mac: Optional[MacSettingsDto] = None
    md: Optional[MdSettingsDto] = None
    mif: Optional[MifSettingsDto] = None
    multilingualXls: Optional[MultilingualXlsSettingsDto] = None
    multilingualCsv: Optional[MultilingualCsvSettingsDto] = None
    multilingualXml: Optional[MultilingualXmlSettingsDto] = None
    pdf: Optional[PdfSettingsDto] = None
    php: Optional[PhpSettingsDto] = None
    po: Optional[PoSettingsDto] = None
    ppt: Optional[PptSettingsDto] = None
    properties: Optional[PropertiesSettingsDto] = None
    psd: Optional[PsdSettingsDto] = None
    quarkTag: Optional[QuarkTagSettingsDto] = None
    resx: Optional[ResxSettingsDto] = None
    sdlXlf: Optional[SdlXlfSettingsDto] = None
    tmMatch: Optional[TMMatchSettingsDto] = None
    ttx: Optional[TtxSettingsDto] = None
    txt: Optional[TxtSettingsDto] = None
    xlf2: Optional[Xlf2SettingsDto] = None
    xlf: Optional[XlfSettingsDto] = None
    xls: Optional[XlsSettingsDto] = None
    xml: Optional[XmlSettingsDto] = None
    yaml: Optional[YamlSettingsDto] = None
    asciidoc: Optional[AsciidocSettingsDto] = None


class Type5(Enum):
    html = "html"
    json = "json"
    xml = "xml"
    multiling_xml = "multiling_xml"
    txt = "txt"


class UpdateCustomFileTypeDto(BaseModel):
    name: Optional[str] = None
    filenamePattern: Optional[str] = None
    type: Optional[Type5] = None
    fileImportSettings: Optional[FileImportSettingsCreateDto] = None


class DeleteCustomFileTypeDto(BaseModel):
    customFileTypes: List[UidReference]


class DiscountSettingsDto(BaseModel):
    repetition: Optional[float] = None
    tm101: Optional[float] = None
    tm100: Optional[float] = None
    tm95: Optional[float] = None
    tm85: Optional[float] = None
    tm75: Optional[float] = None
    tm50: Optional[float] = None
    tm0: Optional[float] = None
    mt100: Optional[float] = None
    mt95: Optional[float] = None
    mt85: Optional[float] = None
    mt75: Optional[float] = None
    mt50: Optional[float] = None
    mt0: Optional[float] = None
    nt100: Optional[float] = None
    nt99: Optional[float] = None
    nt85: Optional[float] = None
    nt75: Optional[float] = None
    nt50: Optional[float] = None
    nt0: Optional[float] = None
    if100: Optional[float] = None
    if95: Optional[float] = None
    if85: Optional[float] = None
    if75: Optional[float] = None
    if50: Optional[float] = None
    if0: Optional[float] = None


class NetRateSchemeWorkflowStepReference(BaseModel):
    id: Optional[str] = None
    workflowStep: Optional[WorkflowStepReference] = None


class PageDtoNetRateSchemeReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[NetRateSchemeReference]] = None


class NetRateSchemeWorkflowStepCreate(BaseModel):
    workflowStep: IdReference
    rates: Optional[DiscountSettingsDto] = None


class NetRateSchemeEdit(BaseModel):
    name: constr(min_length=1, max_length=255)
    rates: Optional[DiscountSettingsDto] = None


class NetRateSchemeWorkflowStep(BaseModel):
    id: Optional[str] = None
    workflowStep: Optional[WorkflowStepReference] = None
    rates: Optional[DiscountSettingsDto] = None


class NetRateSchemeWorkflowStepEdit(BaseModel):
    rates: Optional[DiscountSettingsDto] = None


class PageDtoNetRateSchemeWorkflowStepReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[NetRateSchemeWorkflowStepReference]] = None


class DomainDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[UserReference] = None


class PageDtoDomainDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[DomainDto]] = None


class DomainEditDto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None


class Type6(Enum):
    JobAssigned = "JobAssigned"
    JobStatusChanged = "JobStatusChanged"
    NextWorkflowStep = "NextWorkflowStep"
    JobRejected = "JobRejected"
    LoginInfo = "LoginInfo"
    ProjectTransferredToBuyer = "ProjectTransferredToBuyer"
    SharedProjectAssigned = "SharedProjectAssigned"
    SharedProjectStatusChanged = "SharedProjectStatusChanged"
    AutomatedProjectCreated = "AutomatedProjectCreated"
    AutomatedProjectSourceUpdated = "AutomatedProjectSourceUpdated"
    AutomatedProjectStatusChanged = "AutomatedProjectStatusChanged"
    JobWidgetProjectQuotePrepared = "JobWidgetProjectQuotePrepared"
    JobWidgetProjectQuotePreparationFailure = "JobWidgetProjectQuotePreparationFailure"
    JobWidgetProjectCreated = "JobWidgetProjectCreated"
    JobWidgetProjectCompleted = "JobWidgetProjectCompleted"
    CmsQuoteReady = "CmsQuoteReady"
    CmsWorkCompleted = "CmsWorkCompleted"
    CmsJobRejected = "CmsJobRejected"
    QUOTE_UPDATED = "QUOTE_UPDATED"
    QUOTE_STATUS_CHANGED = "QUOTE_STATUS_CHANGED"
    LQA_SHARE_REPORT = "LQA_SHARE_REPORT"


class OrganizationEmailTemplateDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    type: Optional[Type6] = None
    name: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    ccAddress: Optional[str] = None
    bccAddress: Optional[str] = None


class PageDtoOrganizationEmailTemplateDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[OrganizationEmailTemplateDto]] = None


class FileHandoverDto(BaseModel):
    fileId: Optional[str] = Field(None, description="ID of the uploaded file")
    filename: Optional[str] = Field(None, description="Filename of the uploaded file")


class JobPartReferences(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)


class UploadedFileDto(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    size: Optional[int] = None
    type: Optional[str] = None


class PageDtoUploadedFileDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[UploadedFileDto]] = None


class RemoteUploadedFileDto(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    size: Optional[int] = None
    type: Optional[str] = None
    url: Optional[str] = None


class MachineTranslateSettingsLangsDto(BaseModel):
    id: Optional[str] = Field(None, description="Id")
    sourceLang: Optional[str] = Field(
        None, description="Source language for CUSTOMIZABLE engine"
    )
    targetLangs: Optional[List[str]] = Field(
        None, description="List of target languages for the CUSTOMIZABLE engine"
    )


class MemTransMachineTranslateSettingsDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    baseName: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    category: Optional[str] = None
    default_: Optional[bool] = None
    includeTags: Optional[bool] = None
    mtQualityEstimation: Optional[bool] = None
    enabled: Optional[bool] = None
    glossarySupported: Optional[bool] = None
    args: Optional[Dict[str, str]] = None
    langs: Optional[MachineTranslateSettingsLangsDto] = None
    charCount: Optional[int] = Field(
        None, description="Unknown value is represented by value: -1"
    )


class MemsourceTranslateProfileSimpleDto(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    memsourceTranslate: Optional[MemTransMachineTranslateSettingsDto] = None
    locked: Optional[bool] = None


class GlossaryEditDto(BaseModel):
    name: constr(min_length=0, max_length=255)
    langs: List[str] = Field(..., max_items=2147483647, min_items=1)
    owner: Optional[IdReference] = Field(
        None, description="Owner of the TM must be Admin or PM"
    )


class GlossaryActivationDto(BaseModel):
    active: Optional[bool] = None


class SearchTMClientDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class SearchTMDomainDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class SearchTMProjectDto(BaseModel):
    id: Optional[int] = None
    uid: Optional[str] = None
    name: Optional[str] = None


class SearchTMSubDomainDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class SearchTMTransMemoryDto(BaseModel):
    uid: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    reverse: Optional[bool] = None


class TagMetadata(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    content: Optional[str] = None
    transAttributes: Optional[str] = None


class TagMetadataDto(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    content: Optional[str] = None
    transAttributes: Optional[str] = None


class LanguageDto(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    rfc: Optional[str] = None
    android: Optional[str] = None
    androidBcp: Optional[str] = None


class LanguageListDto(BaseModel):
    languages: List[LanguageDto]


class PassFailThresholdDto(BaseModel):
    minScorePercentage: float = Field(
        ...,
        description="Minimum allowed LQA score in percentage in line with MQM scoring (1 - penalties/word-count)",
        example=99.0,
    )


class SeverityDto(BaseModel):
    code: Optional[int] = Field(None, description="Code of the severity category")
    value: Optional[float] = Field(None, description="Allowed values 0.0-100,000.0")


class ToggleableWeightDto(BaseModel):
    enabled: Optional[bool] = Field(
        None, description="If this error category is enabled, default false"
    )
    weight: Optional[float] = Field(
        None, description="Weight of this error category (0.1 - 99.9)", example=1.0
    )
    code: Optional[int] = Field(None, description="Code of the error category")


class VerityWeightsDto(BaseModel):
    verity: Optional[ToggleableWeightDto] = None
    cultureSpecificReference: Optional[ToggleableWeightDto] = None


class LqaProfileReferenceDto(BaseModel):
    uid: str = Field(..., description="UID of the profile", example="string")
    name: str = Field(..., description="Name of the profile")
    isDefault: bool = Field(
        ..., description="If profile is set as default for organization"
    )
    createdBy: UserReference = Field(..., description="User who created the profile")
    dateCreated: datetime = Field(..., description="When profile was created")
    organization: UidReference


class PageDtoLqaProfileReferenceDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[LqaProfileReferenceDto]] = None


class MachineTranslateStatusDto(BaseModel):
    uid: Optional[str] = None
    ok: Optional[bool] = None
    error: Optional[str] = None


class MachineTranslateSettingsPbmDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    baseName: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    default_: Optional[bool] = None
    includeTags: Optional[bool] = None
    mtQualityEstimation: Optional[bool] = None
    args: Optional[Dict[str, str]] = None
    payForMtPossible: Optional[bool] = None
    payForMtActive: Optional[bool] = None
    charCount: Optional[int] = None
    sharingSettings: Optional[int] = None
    langs: Optional[MachineTranslateSettingsLangsDto] = None


class PageDtoMachineTranslateSettingsPbmDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[MachineTranslateSettingsPbmDto]] = None


class MachineTranslateSettingsDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    baseName: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    category: Optional[str] = None
    default_: Optional[bool] = None
    includeTags: Optional[bool] = None
    mtQualityEstimation: Optional[bool] = None
    enabled: Optional[bool] = None
    args: Optional[Dict[str, str]] = None
    langs: Optional[MachineTranslateSettingsLangsDto] = None


class TypesDto(BaseModel):
    types: Optional[List[str]] = None


class MachineTranslateResponse(BaseModel):
    translations: Optional[List[str]] = None


class TranslationRequestExtendedDto(BaseModel):
    sourceTexts: List[str] = Field(..., max_items=2147483647, min_items=1)
    from_: str = Field(..., alias="from")
    to: str
    filename: Optional[str] = None


class MachineTranslateSettingsReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class ProjectTermBaseReference(BaseModel):
    id: Optional[str] = None
    termBase: Optional[ObjectReference] = None
    name: Optional[str] = None
    writeMode: Optional[bool] = None
    targetLang: Optional[str] = None
    readMode: Optional[bool] = None
    workflowStep: Optional[ObjectReference] = None


class ProjectTranslationMemoryReference(BaseModel):
    id: Optional[str] = None
    transMem: Optional[ObjectReference] = None
    name: Optional[str] = None
    workflowStep: Optional[ObjectReference] = None
    targetLang: Optional[str] = None
    penalty: Optional[float] = None
    readMode: Optional[bool] = None


class TaskMappingDto(BaseModel):
    taskId: Optional[str] = None
    workflowLevel: Optional[str] = None
    resourcePath: Optional[str] = None
    project: Optional[ObjectReference] = None
    job: Optional[ObjectReference] = None


class ImportSettingsEditDto(BaseModel):
    uid: str
    name: str
    fileImportSettings: FileImportSettingsCreateDto


class ImportSettingsReference(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None


class PageDtoImportSettingsReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[ImportSettingsReference]] = None


class ImportSettingsCreateDto(BaseModel):
    name: str
    fileImportSettings: FileImportSettingsCreateDto


class BusinessUnitReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None


class DiscountSchemeReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None


class DomainReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None


class SubDomainReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None


class FileNamingSettingsDto(BaseModel):
    renameCompleted: Optional[bool] = None
    completedFilePattern: Optional[constr(min_length=0, max_length=255)] = None
    targetFolderPath: Optional[constr(min_length=0, max_length=255)] = None


class VendorSecuritySettingsDto(BaseModel):
    canChangeSharedJobDueDate: Optional[List[UidReference]] = None
    jobVendorsMayUploadReferences: Optional[bool] = Field(
        None, description="Default: `false`"
    )


class MachineTranslationSettingsDto(BaseModel):
    useMachineTranslation: Optional[bool] = Field(
        None, description="Pre-translate from machine translation. Default: false"
    )
    lock100PercentMatches: Optional[bool] = Field(
        None,
        description="Lock section: 100% machine translation matches. Default: false",
    )
    confirm100PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 100% translation machine matches. Default: false",
    )
    useAltTransOnly: Optional[bool] = Field(
        None,
        description="Do not put machine translations to target and use alt-trans fields (alt-trans in mxlf).\nDefault: false",
    )
    mtQeMatchesInEditors: Optional[bool] = Field(
        None,
        description="Display quality-estimated machine translation matches in Memsource Editor. Default: false",
    )
    mtForTMAbove100: Optional[bool] = Field(
        None,
        description="Use machine translation for segments with a TM match of 100% or more. Default: false",
    )


class NonTranslatableSettingsDto(BaseModel):
    preTranslateNonTranslatables: Optional[bool] = Field(
        None, description="Pre-translate non-translatables. Default: false"
    )
    confirm100PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 100% non-translatable matches. Default: false",
    )
    lock100PercentMatches: Optional[bool] = Field(
        None, description="Lock section: 100% non-translatable matches. Default: false"
    )
    nonTranslatablesInEditors: Optional[bool] = Field(
        None, description="If non-translatables are enabled in Editors."
    )


class RepetitionsSettingsDto(BaseModel):
    autoPropagateRepetitions: Optional[bool] = Field(
        None, description="Propagate repetitions. Default: false"
    )
    confirmRepetitions: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: Repetitions. Default: false",
    )
    autoPropagateToLockedRepetitions: Optional[bool] = Field(
        None,
        description="Changes in 1st repetition propagate upon confirmation into subsequent locked repetitions. Default: false",
    )
    lockSubsequentRepetitions: Optional[bool] = Field(
        None,
        description="If auto-propagated subsequent repetitions should be locked. Default: false",
    )


class TranslationMemorySettingsDto(BaseModel):
    useTranslationMemory: Optional[bool] = Field(
        None, description="Pre-translate from translation memory. Default: false"
    )
    translationMemoryThreshold: Optional[confloat(ge=0.0, le=1.01)] = Field(
        None, description="Pre-translation threshold percent"
    )
    confirm100PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 100% translation memory matches. Default: false",
    )
    confirm101PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 101% translation memory matches. Default: false",
    )
    lock100PercentMatches: Optional[bool] = Field(
        None,
        description="Lock section: 100% translation memory matches. Default: false",
    )
    lock101PercentMatches: Optional[bool] = Field(
        None,
        description="Lock section: 101% translation memory matches. Default: false",
    )


class Number(BaseModel):
    pass


class Type7(Enum):
    VOID = "VOID"
    NUMBER = "NUMBER"
    STRING = "STRING"
    REGEX = "REGEX"
    MORAVIA = "MORAVIA"


class Name1(Enum):
    emptyTarget = "emptyTarget"
    inconsistentTranslation = "inconsistentTranslation"
    joinMarksInconsistency = "joinMarksInconsistency"
    missingNumber = "missingNumber"
    segmentNotConfirmed = "segmentNotConfirmed"
    nonConformingTerms = "nonConformingTerms"
    multipleSpaces = "multipleSpaces"
    endPunctuation = "endPunctuation"
    targetLength = "targetLength"
    absoluteTargetLength = "absoluteTargetLength"
    relativeTargetLength = "relativeTargetLength"
    inconsistentFormatting = "inconsistentFormatting"
    unresolvedComment = "unresolvedComment"
    emptyPairTags = "emptyPairTags"
    strictJobStatus = "strictJobStatus"
    forbiddenStringsEnabled = "forbiddenStringsEnabled"
    excludeLockedSegments = "excludeLockedSegments"
    ignoreNotApprovedTerms = "ignoreNotApprovedTerms"
    spellCheck = "spellCheck"
    repeatedWords = "repeatedWords"
    inconsistentTagContent = "inconsistentTagContent"
    emptyTagContent = "emptyTagContent"
    malformed = "malformed"
    forbiddenTerms = "forbiddenTerms"
    targetLengthPercent = "targetLengthPercent"
    targetLengthPerSegment = "targetLengthPerSegment"
    newerAtLowerLevel = "newerAtLowerLevel"
    leadingAndTrailingSpaces = "leadingAndTrailingSpaces"
    targetSourceIdentical = "targetSourceIdentical"
    ignoreInAllWorkflowSteps = "ignoreInAllWorkflowSteps"
    regexp = "regexp"
    unmodifiedFuzzyTranslation = "unmodifiedFuzzyTranslation"
    unmodifiedFuzzyTranslationTM = "unmodifiedFuzzyTranslationTM"
    unmodifiedFuzzyTranslationMTNT = "unmodifiedFuzzyTranslationMTNT"
    moravia = "moravia"
    extraNumbers = "extraNumbers"
    nestedTags = "nestedTags"


class QACheckDtoV2(BaseModel):
    type: Type7
    name: Name1


class QASettingsDtoV2(BaseModel):
    checks: Optional[List[QACheckDtoV2]] = None


class RegexpCheckRuleDtoV2(BaseModel):
    description: Optional[str] = None
    sourceRegexp: Optional[str] = None
    targetRegexp: Optional[str] = None
    id: Optional[str] = None
    ignorable: Optional[bool] = None
    instant: Optional[bool] = None


class STRING(QACheckDtoV2):
    ignorable: Optional[bool] = None
    enabled: Optional[bool] = None
    value: Optional[str] = None
    instant: Optional[bool] = None


class VOID(QACheckDtoV2):
    ignorable: Optional[bool] = None
    enabled: Optional[bool] = None
    instant: Optional[bool] = None


class EditQASettingsDtoV2(BaseModel):
    checks: Optional[List[Dict[str, Dict[str, Any]]]] = Field(
        None,
        description="checks",
        example='\n        {\n            "ignorable": false,\n            "enabled": true,\n            "type": "VOID",\n            "instant": false,\n            "name": "emptyTarget"\n        },\n        {\n            "ignorable": false,\n            "enabled": true,\n            "value": 12,\n            "type": "NUMBER",\n            "name": "targetLength"\n        },\n        {\n            "ignorable": false,\n            "enabled": true,\n            "value": "ASAP, irony",\n            "type": "STRING",\n            "instant": true,\n            "name": "forbiddenStrings"\n        },\n        {\n            "enabled": true,\n            "profile": "jiris",\n            "ignorable": true,\n            "type": "MORAVIA",\n            "name": "moravia"\n        },\n        {\n            "rules": [\n                {\n                    "description": "Description",\n                    "sourceRegexp": ".+",\n                    "targetRegexp": ".+",\n                    "ignorable": true\n                },\n                {\n                    "description": "Description",\n                    "sourceRegexp": "i+",\n                    "targetRegexp": "e+",\n                    "ignorable": false\n                }\n            ],\n            "type": "REGEX",\n            "name": "regexp"\n        }\n    ',
    )


class Status1(Enum):
    resolved = "resolved"
    unresolved = "unresolved"


class EditPlainConversationDto(BaseModel):
    status: Optional[Status1] = None
    correlation: Optional[ReferenceCorrelation] = None


class Status2(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class Status3(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class BuyerReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None


class CostCenterReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None


class MTSettingsPerLanguageReference(BaseModel):
    targetLang: Optional[str] = Field(
        None, description="mtSettings is set for whole project if targetLang == null"
    )
    machineTranslateSettings: Optional[MachineTranslateSettingsReference] = None


class ProgressDto(BaseModel):
    totalCount: Optional[int] = None
    finishedCount: Optional[int] = None
    overdueCount: Optional[int] = None


class ProjectWorkflowStepDto(BaseModel):
    id: Optional[int] = None
    abbreviation: Optional[str] = None
    name: Optional[str] = None
    workflowLevel: Optional[int] = None
    workflowStep: Optional[ObjectReference] = None
    lqaProfileUid: Optional[str] = None


class ReferenceFileReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    filename: Optional[str] = None
    note: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None


class Status4(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class VendorReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None


class ProjectMTSettingsPerLangDto(BaseModel):
    targetLang: str
    machineTranslateSettings: Optional[UidReference] = None


class Status5(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class PatchProjectDto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None
    status: Optional[Status5] = None
    client: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    owner: Optional[IdReference] = None
    purchaseOrder: Optional[constr(min_length=0, max_length=255)] = None
    dateDue: Optional[datetime] = None
    note: Optional[constr(min_length=0, max_length=4096)] = None
    machineTranslateSettings: Optional[UidReference] = None
    machineTranslateSettingsPerLangs: Optional[List[ProjectMTSettingsPerLangDto]] = None
    archived: Optional[bool] = None


class AddTargetLangDto(BaseModel):
    targetLangs: List[str] = Field(..., max_items=2147483647, min_items=1)


class AddWorkflowStepsDto(BaseModel):
    workflowSteps: List[IdReference] = Field(..., max_items=2147483647, min_items=1)


class AssignVendorDto(BaseModel):
    vendor: Optional[IdReference] = None
    dateDue: Optional[datetime] = None


class CloneProjectDto(BaseModel):
    name: str


class PageDtoProviderReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[ProviderReference]] = None


class Status6(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class SetProjectStatusDto(BaseModel):
    status: Status6


class ProjectTemplateWorkflowSettingsAssignedToDto(BaseModel):
    targetLang: Optional[str] = None
    providers: Optional[List[ProviderReference]] = None


class FinancialSettingsDto(BaseModel):
    netRateScheme: Optional[NetRateSchemeReference] = None
    priceList: Optional[PriceListReference] = None


class SetFinancialSettingsDto(BaseModel):
    netRateScheme: Optional[IdReference] = None
    priceList: Optional[IdReference] = None


class EnabledCheck(Enum):
    EmptyTranslation = "EmptyTranslation"
    TrailingPunctuation = "TrailingPunctuation"
    Formatting = "Formatting"
    JoinTags = "JoinTags"
    MissingNumbersV3 = "MissingNumbersV3"
    MultipleSpacesV3 = "MultipleSpacesV3"
    NonConformingTerm = "NonConformingTerm"
    NotConfirmed = "NotConfirmed"
    TranslationLength = "TranslationLength"
    AbsoluteLength = "AbsoluteLength"
    RelativeLength = "RelativeLength"
    UnresolvedComment = "UnresolvedComment"
    EmptyPairTags = "EmptyPairTags"
    InconsistentTranslationTargetSource = "InconsistentTranslationTargetSource"
    InconsistentTranslationSourceTarget = "InconsistentTranslationSourceTarget"
    ForbiddenString = "ForbiddenString"
    SpellCheck = "SpellCheck"
    RepeatedWord = "RepeatedWord"
    InconsistentTagContent = "InconsistentTagContent"
    EmptyTagContent = "EmptyTagContent"
    Malformed = "Malformed"
    ForbiddenTerm = "ForbiddenTerm"
    NewerAtLowerLevel = "NewerAtLowerLevel"
    LeadingAndTrailingSpaces = "LeadingAndTrailingSpaces"
    LeadingSpaces = "LeadingSpaces"
    TrailingSpaces = "TrailingSpaces"
    TargetSourceIdentical = "TargetSourceIdentical"
    SourceOrTargetRegexp = "SourceOrTargetRegexp"
    UnmodifiedFuzzyTranslation = "UnmodifiedFuzzyTranslation"
    UnmodifiedFuzzyTranslationTM = "UnmodifiedFuzzyTranslationTM"
    UnmodifiedFuzzyTranslationMTNT = "UnmodifiedFuzzyTranslationMTNT"
    Moravia = "Moravia"
    ExtraNumbersV3 = "ExtraNumbersV3"
    UnresolvedConversation = "UnresolvedConversation"
    NestedTags = "NestedTags"


class EnabledQualityChecksDto(BaseModel):
    enabledChecks: Optional[List[EnabledCheck]] = None


class LqaErrorCategoryDto(BaseModel):
    errorCategoryId: Optional[int] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    errorCategories: Optional[List[LqaErrorCategoryDto]] = None


class LqaSeverityDto(BaseModel):
    severityId: Optional[int] = None
    name: Optional[str] = None
    weight: Optional[int] = None


class MTSettingsPerLanguageDto(BaseModel):
    targetLang: str = Field(
        ..., description="mtSettings is set for whole project if targetLang == null"
    )
    machineTranslateSettings: Optional[MachineTranslateSettingsDto] = None


class MTSettingsPerLanguageListDto(BaseModel):
    mtSettingsPerLangList: Optional[List[MTSettingsPerLanguageDto]] = Field(
        None, unique_items=True
    )


class Status7(Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    DRAFT = "DRAFT"
    FOR_APPROVAL = "FOR_APPROVAL"
    NEW = "NEW"


class BillingUnit(Enum):
    Character = "Character"
    Word = "Word"
    Page = "Page"
    Hour = "Hour"


class QuoteType(Enum):
    BUYER = "BUYER"
    PROVIDER = "PROVIDER"


class QuoteDto(BaseModel):
    id: Optional[int] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    status: Optional[Status7] = None
    currency: Optional[str] = None
    billingUnit: Optional[BillingUnit] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    totalPrice: Optional[float] = None
    netRateScheme: Optional[NetRateSchemeReference] = None
    priceList: Optional[PriceListReference] = None
    workflowStepList: Optional[List[WorkflowStepReference]] = None
    provider: Optional[ProviderReference] = None
    customerEmail: Optional[str] = None
    quoteType: Optional[QuoteType] = None
    editable: Optional[bool] = None
    outdated: Optional[bool] = None


class EditProjectMTSettPerLangDto(BaseModel):
    targetLang: str
    machineTranslateSettings: Optional[IdReference] = None


class EditProjectMTSettPerLangListDto(BaseModel):
    mtSettingsPerLangList: Optional[List[EditProjectMTSettPerLangDto]] = None


class EditProjectMTSettingsDto(BaseModel):
    machineTranslateSettings: Optional[IdReference] = None


class Type8(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    PreAnalyseTarget = "PreAnalyseTarget"
    Compare = "Compare"


class AnalyseSettingsDto(BaseModel):
    type: Optional[Type8] = None
    includeFuzzyRepetitions: Optional[bool] = Field(None, description="Default: false")
    separateFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    includeNonTranslatables: Optional[bool] = Field(None, description="Default: false")
    includeMachineTranslationMatches: Optional[bool] = Field(
        None, description="Default: false"
    )
    includeConfirmedSegments: Optional[bool] = Field(None, description="Default: false")
    includeNumbers: Optional[bool] = Field(None, description="Default: false")
    includeLockedSegments: Optional[bool] = Field(None, description="Default: false")
    countSourceUnits: Optional[bool] = Field(None, description="Default: false")
    includeTransMemory: Optional[bool] = Field(None, description="Default: false")
    namingPattern: Optional[str] = None
    analyzeByLanguage: Optional[bool] = Field(None, description="Default: false")
    analyzeByProvider: Optional[bool] = Field(None, description="Default: false")
    allowAutomaticPostAnalysis: Optional[bool] = Field(
        None,
        description="If automatic post analysis should be created after update source. Default: false",
    )


class Providers(BaseModel):
    all: Optional[List[ProviderReference]] = None
    relevant: Optional[List[ProviderReference]] = None


class SplitJobActionDto(BaseModel):
    segmentOrdinals: List[int] = Field(..., max_items=2147483647, min_items=1)
    partCount: Optional[int] = None
    partSize: Optional[int] = None
    wordCount: Optional[int] = None
    byDocumentPart: Optional[bool] = Field(
        None, description="Can be used only for PowerPoint files"
    )


class RequestedStatus(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobStatusChangeActionDto(BaseModel):
    requestedStatus: Optional[RequestedStatus] = None
    notifyOwner: Optional[bool] = Field(
        None,
        description="Default: false; Both project owner and job owner are notified;\n                    the parameter is subordinated to notification settings in the project",
    )
    propagateStatus: Optional[bool] = Field(
        None,
        description="Default: false;\n        Controls both job status and email notifications to previous/next provider",
    )


class ContinuousJobInfoDto(BaseModel):
    dateUpdated: Optional[datetime] = None


class Status8(Enum):
    RUNNING = "RUNNING"
    ERROR = "ERROR"
    OK = "OK"


class ImportStatusDto(BaseModel):
    status: Optional[Status8] = None
    errorMessage: Optional[str] = None


class Status9(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobReference(BaseModel):
    uid: Optional[str] = None
    filename: Optional[str] = None


class ProjectWorkflowStepReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    order: Optional[int] = None
    workflowLevel: Optional[int] = None


class JobPartReadyReferences(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    getParts: Optional[Dict[str, Any]] = None


class SubstituteDto(BaseModel):
    source: str
    target: str


class Status10(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartStatusChangeDto(BaseModel):
    status: Optional[Status10] = None
    changedDate: Optional[datetime] = None
    changedBy: Optional[UserReference] = None


class JobPartStatusChangesDto(BaseModel):
    statusChanges: Optional[List[JobPartStatusChangeDto]] = None


class Status11(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartUpdateSingleDto(BaseModel):
    status: Status11
    dateDue: Optional[datetime] = None
    providers: Optional[List[ProviderReference]] = None


class Status12(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartPatchSingleDto(BaseModel):
    status: Optional[Status12] = None
    dateDue: Optional[datetime] = None
    providers: Optional[List[ProviderReference]] = None


class TranslationResourcesDto(BaseModel):
    machineTranslateSettings: Optional[MachineTranslateSettingsReference] = None
    translationMemories: Optional[List[ProjectTranslationMemoryReference]] = None
    termBases: Optional[List[ProjectTermBaseReference]] = None


class WorkflowStepDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    abbr: Optional[str] = None
    order: Optional[int] = None
    lqaEnabled: Optional[bool] = None


class TargetFileWarningsDto(BaseModel):
    warnings: Optional[List[str]] = None


class Type9(Enum):
    ORIGINAL = "ORIGINAL"
    PDF = "PDF"


class PreviewUrlDto(BaseModel):
    type: Optional[Type9] = None
    url: Optional[str] = None


class PreviewUrlsDto(BaseModel):
    previews: Optional[List[PreviewUrlDto]] = None


class Action1(Enum):
    PRE_ANALYSE = "PRE_ANALYSE"
    POST_ANALYSE = "POST_ANALYSE"
    COMPARE_ANALYSE = "COMPARE_ANALYSE"
    PARENT_ANALYSE = "PARENT_ANALYSE"
    PRE_TRANSLATE = "PRE_TRANSLATE"
    ASYNC_TRANSLATE = "ASYNC_TRANSLATE"
    IMPORT_JOB = "IMPORT_JOB"
    IMPORT_FILE = "IMPORT_FILE"
    ALIGN = "ALIGN"
    EXPORT_TMX_BY_QUERY = "EXPORT_TMX_BY_QUERY"
    EXPORT_TMX = "EXPORT_TMX"
    IMPORT_TMX = "IMPORT_TMX"
    INSERT_INTO_TM = "INSERT_INTO_TM"
    DELETE_TM = "DELETE_TM"
    CLEAR_TM = "CLEAR_TM"
    QA = "QA"
    QA_V3 = "QA_V3"
    UPDATE_CONTINUOUS_JOB = "UPDATE_CONTINUOUS_JOB"
    UPDATE_SOURCE = "UPDATE_SOURCE"
    UPDATE_TARGET = "UPDATE_TARGET"
    EXTRACT_CLEANED_TMS = "EXTRACT_CLEANED_TMS"
    GLOSSARY_PUT = "GLOSSARY_PUT"
    GLOSSARY_DELETE = "GLOSSARY_DELETE"
    CREATE_PROJECT = "CREATE_PROJECT"
    EXPORT_COMPLETE_FILE = "EXPORT_COMPLETE_FILE"


class AsyncRequestReference(BaseModel):
    id: Optional[str] = None
    dateCreated: Optional[datetime] = None
    action: Optional[Action1] = None


class JobCreateRemoteFileDto(BaseModel):
    connectorToken: str
    remoteFolder: Optional[str] = None
    remoteFileName: str
    remoteFileNameRegex: Optional[bool] = None
    continuous: Optional[bool] = None


class NotifyProviderDto(BaseModel):
    organizationEmailTemplate: IdReference
    notificationIntervalInMinutes: Optional[conint(ge=0, le=1440)] = None


class User(BaseModel):
    id: int


class Status13(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartUpdateSourceDto(BaseModel):
    uid: Optional[str] = None
    status: Optional[Status13] = None
    targetLang: Optional[str] = None
    filename: Optional[str] = None
    workflowLevel: Optional[int] = None
    workflowStep: Optional[WorkflowStepReference] = None


class JobUpdateSourceResponseDto(BaseModel):
    asyncRequest: Optional[AsyncRequestReference] = None
    jobs: Optional[List[JobPartUpdateSourceDto]] = None


class JobPartDeleteReferences(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    getParts: Optional[Dict[str, Any]] = None


class Level(Enum):
    STANDARD = "STANDARD"
    PRO = "PRO"


class HumanTranslateJobsDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    humanTranslateSettings: IdReference
    comment: Optional[str] = None
    glossaryId: Optional[str] = None
    usePreferredTranslators: Optional[bool] = None
    level: Optional[Level] = None
    callbackUrl: Optional[str] = None


class NotifyJobPartsRequestDto(BaseModel):
    jobs: List[UidReference]
    emailTemplate: IdReference
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None


class GetBilingualFileDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=1000, min_items=1)


class Status14(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartUpdateBatchDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    status: Status14
    dateDue: Optional[datetime] = None
    providers: Optional[List[ProviderReference]] = None


class SegmentReference(BaseModel):
    uid: Optional[str] = None


class WarningType(Enum):
    EmptyTranslation = "EmptyTranslation"
    TrailingPunctuation = "TrailingPunctuation"
    Formatting = "Formatting"
    JoinTags = "JoinTags"
    MissingNumbersV3 = "MissingNumbersV3"
    MultipleSpacesV3 = "MultipleSpacesV3"
    NonConformingTerm = "NonConformingTerm"
    NotConfirmed = "NotConfirmed"
    TranslationLength = "TranslationLength"
    AbsoluteLength = "AbsoluteLength"
    RelativeLength = "RelativeLength"
    UnresolvedComment = "UnresolvedComment"
    EmptyPairTags = "EmptyPairTags"
    InconsistentTranslationTargetSource = "InconsistentTranslationTargetSource"
    InconsistentTranslationSourceTarget = "InconsistentTranslationSourceTarget"
    ForbiddenString = "ForbiddenString"
    SpellCheck = "SpellCheck"
    RepeatedWord = "RepeatedWord"
    InconsistentTagContent = "InconsistentTagContent"
    EmptyTagContent = "EmptyTagContent"
    Malformed = "Malformed"
    ForbiddenTerm = "ForbiddenTerm"
    NewerAtLowerLevel = "NewerAtLowerLevel"
    LeadingAndTrailingSpaces = "LeadingAndTrailingSpaces"
    LeadingSpaces = "LeadingSpaces"
    TrailingSpaces = "TrailingSpaces"
    TargetSourceIdentical = "TargetSourceIdentical"
    SourceOrTargetRegexp = "SourceOrTargetRegexp"
    UnmodifiedFuzzyTranslation = "UnmodifiedFuzzyTranslation"
    UnmodifiedFuzzyTranslationTM = "UnmodifiedFuzzyTranslationTM"
    UnmodifiedFuzzyTranslationMTNT = "UnmodifiedFuzzyTranslationMTNT"
    Moravia = "Moravia"
    ExtraNumbersV3 = "ExtraNumbersV3"
    UnresolvedConversation = "UnresolvedConversation"
    NestedTags = "NestedTags"


class UpdateIgnoredChecksDto(BaseModel):
    segment: SegmentReference
    warningTypes: List[WarningType] = Field(..., max_items=100, min_items=1)


class UpdateIgnoredWarning(BaseModel):
    id: str


class SearchJobsRequestDto(BaseModel):
    jobs: List[UidReference] = Field(
        ..., description="Max: 50 records", max_items=50, min_items=1
    )


class QualityAssuranceDto(BaseModel):
    segmentsCount: Optional[int] = None
    warningsCount: Optional[int] = None
    ignoredWarningsCount: Optional[int] = None


class SegmentsCountsDto(BaseModel):
    allConfirmed: Optional[bool] = None
    charsCount: Optional[int] = None
    completedCharsCount: Optional[int] = None
    confirmedCharsCount: Optional[int] = None
    confirmedLockedCharsCount: Optional[int] = None
    lockedCharsCount: Optional[int] = None
    segmentsCount: Optional[int] = None
    completedSegmentsCount: Optional[int] = None
    lockedSegmentsCount: Optional[int] = None
    segmentGroupsCount: Optional[int] = None
    translatedSegmentsCount: Optional[int] = None
    translatedLockedSegmentsCount: Optional[int] = None
    wordsCount: Optional[int] = None
    completedWordsCount: Optional[int] = None
    confirmedWordsCount: Optional[int] = None
    confirmedLockedWordsCount: Optional[int] = None
    lockedWordsCount: Optional[int] = None
    addedSegments: Optional[int] = None
    addedWords: Optional[int] = None
    machineTranslationPostEditedSegmentsCount: Optional[int] = None
    machineTranslationRelevantSegmentsCount: Optional[int] = None
    qualityAssurance: Optional[QualityAssuranceDto] = None
    qualityAssuranceResolved: Optional[bool] = None


class Status15(Enum):
    RUNNING = "RUNNING"
    ERROR = "ERROR"
    OK = "OK"


class ImportStatusDtoV2(BaseModel):
    status: Optional[Status15] = None
    errorMessage: Optional[str] = None


class Status16(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartReferenceV2(BaseModel):
    uid: Optional[str] = None
    innerId: Optional[str] = Field(
        None,
        description="InnerId is a sequential number of a job in a project.\n            Jobs created from the same file share the same innerId across workflow steps",
    )
    status: Optional[Status16] = None
    providers: Optional[List[ProviderReference]] = None
    targetLang: Optional[str] = None
    workflowStep: Optional[ProjectWorkflowStepReference] = None
    filename: Optional[str] = None
    originalFileDirectory: Optional[str] = None
    dateDue: Optional[datetime] = None
    dateCreated: Optional[datetime] = None
    importStatus: Optional[ImportStatusDtoV2] = None
    continuous: Optional[bool] = None
    sourceFileUid: Optional[str] = None
    split: Optional[bool] = None
    serverTaskId: Optional[str] = None
    owner: Optional[UserReference] = None
    imported: Optional[bool] = Field(None, description="Default: false")


class PageDtoJobPartReferenceV2(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[JobPartReferenceV2]] = None


class Status17(Enum):
    New = "New"
    Approved = "Approved"


class TermDto(BaseModel):
    id: Optional[str] = None
    text: str
    lang: Optional[str] = None
    rtl: Optional[bool] = None
    modifiedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    modifiedBy: Optional[UserReference] = None
    createdBy: Optional[UserReference] = None
    caseSensitive: Optional[bool] = None
    exactMatch: Optional[bool] = None
    forbidden: Optional[bool] = None
    preferred: Optional[bool] = None
    status: Optional[Status17] = None
    conceptId: Optional[str] = None
    usage: Optional[str] = None
    note: Optional[str] = None
    writable: Optional[bool] = None
    shortTranslation: Optional[str] = None
    termType: Optional[str] = None
    partOfSpeech: Optional[str] = None
    gender: Optional[str] = None
    number: Optional[str] = None
    definition: Optional[str] = None
    domain: Optional[str] = None
    subDomains: Optional[List[str]] = None
    url: Optional[str] = None
    conceptNote: Optional[str] = None


class TermPairDto(BaseModel):
    sourceTerm: TermDto
    targetTerm: TermDto


class TermType(Enum):
    FULL_FORM = "FULL_FORM"
    SHORT_FORM = "SHORT_FORM"
    ACRONYM = "ACRONYM"
    ABBREVIATION = "ABBREVIATION"
    PHRASE = "PHRASE"
    VARIANT = "VARIANT"


class PartOfSpeech(Enum):
    ADJECTIVE = "ADJECTIVE"
    NOUN = "NOUN"
    VERB = "VERB"
    ADVERB = "ADVERB"


class Gender(Enum):
    MASCULINE = "MASCULINE"
    FEMININE = "FEMININE"
    NEUTRAL = "NEUTRAL"


class Number1(Enum):
    SINGULAR = "SINGULAR"
    PLURAL = "PLURAL"
    UNCOUNTABLE = "UNCOUNTABLE"


class TermCreateByJobDto(BaseModel):
    text: str
    caseSensitive: Optional[bool] = Field(None, description="Default: false")
    exactMatch: Optional[bool] = Field(None, description="Default: false")
    forbidden: Optional[bool] = Field(None, description="Default: false")
    preferred: Optional[bool] = Field(None, description="Default: false")
    usage: Optional[str] = None
    note: Optional[str] = None
    shortTranslation: Optional[str] = None
    termType: Optional[TermType] = None
    partOfSpeech: Optional[PartOfSpeech] = None
    gender: Optional[Gender] = None
    number: Optional[Number1] = None


class Match(BaseModel):
    beginIndex: Optional[int] = None
    text: Optional[str] = None


class TermBaseDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    internalId: Optional[int] = None
    name: str
    langs: Optional[List[str]] = None
    client: Optional[ClientReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    createdBy: Optional[UserReference] = None
    owner: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    note: Optional[str] = None
    canShow: Optional[bool] = None


class SearchResponseTbDto(BaseModel):
    termBase: Optional[TermBaseDto] = None
    conceptId: Optional[str] = None
    sourceTerm: Optional[TermDto] = None
    translationTerms: Optional[List[TermDto]] = None


class CreateReferenceFileNoteDto(BaseModel):
    note: str


class ReferenceFileAccessDto(BaseModel):
    canCreate: Optional[bool] = None


class ReferenceFilePageDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[ReferenceFileReference]] = None
    access: Optional[ReferenceFileAccessDto] = None


class ProjectReferenceFilesRequestDto(BaseModel):
    referenceFiles: List[IdReference]


class TransMemoryDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    internalId: Optional[int] = None
    name: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    client: Optional[ClientReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    note: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    owner: Optional[UserReference] = None


class AssignmentPerTargetLangDto(BaseModel):
    targetLang: Optional[str] = None
    providers: Optional[List[ProviderReference]] = None


class ProjectTemplateNotifyProviderDto(BaseModel):
    organizationEmailTemplate: ObjectReference
    notificationIntervalInMinutes: Optional[conint(ge=0, le=1440)] = None


class WorkflowStepSettingsDto(BaseModel):
    workflowStep: Optional[WorkflowStepReference] = None
    assignedTo: Optional[List[ProjectTemplateWorkflowSettingsAssignedToDto]] = None
    notifyProvider: Optional[ProjectTemplateNotifyProviderDto] = None
    lqaProfile: Optional[UidReference] = None


class ProjectTemplateCreateActionDto(BaseModel):
    project: UidReference
    name: constr(min_length=0, max_length=255)
    importSettings: Optional[UidReference] = None
    useDynamicTitle: Optional[bool] = None
    dynamicTitle: Optional[constr(min_length=0, max_length=255)] = None


class ProjectTemplateTermBaseDto(BaseModel):
    targetLocale: Optional[str] = None
    workflowStep: Optional[WorkflowStepReference] = None
    readMode: Optional[bool] = None
    writeMode: Optional[bool] = None
    termBase: Optional[TermBaseDto] = None
    qualityAssurance: Optional[bool] = None


class ProjectTemplateTermBaseListDto(BaseModel):
    termBases: Optional[List[ProjectTemplateTermBaseDto]] = None


class ProjectSecuritySettingsDtoV2(BaseModel):
    downloadEnabled: Optional[bool] = None
    webEditorEnabledForLinguists: Optional[bool] = None
    showUserDataToLinguists: Optional[bool] = None
    emailNotifications: Optional[bool] = None
    strictWorkflowFinish: Optional[bool] = None
    useVendors: Optional[bool] = None
    linguistsMayEditLockedSegments: Optional[bool] = None
    usersMaySetAutoPropagation: Optional[bool] = None
    allowLoadingExternalContentInEditors: Optional[bool] = None
    allowLoadingIframes: Optional[bool] = None
    linguistsMayEditSource: Optional[bool] = None
    linguistsMayEditTagContent: Optional[bool] = None
    linguistsMayDownloadLqaReport: Optional[bool] = None
    usernamesDisplayedInLqaReport: Optional[bool] = None
    userMaySetInstantQA: Optional[bool] = None
    triggerWebhooks: Optional[bool] = None
    vendors: Optional[VendorSecuritySettingsDto] = None
    allowedDomains: Optional[List[str]] = None


class EditProjectSecuritySettingsDtoV2(BaseModel):
    downloadEnabled: Optional[bool] = Field(None, description="Default: `false`")
    webEditorEnabledForLinguists: Optional[bool] = Field(
        None, description="Default: `false`"
    )
    showUserDataToLinguists: Optional[bool] = Field(
        None, description="Default: `false`"
    )
    emailNotifications: Optional[bool] = Field(None, description="Default: `false`")
    strictWorkflowFinish: Optional[bool] = Field(None, description="Default: `false`")
    useVendors: Optional[bool] = Field(None, description="Default: `false`")
    linguistsMayEditLockedSegments: Optional[bool] = Field(
        None, description="Default: `false`"
    )
    usersMaySetAutoPropagation: Optional[bool] = Field(
        None, description="Default: `true`"
    )
    allowLoadingExternalContentInEditors: Optional[bool] = Field(
        None, description="Default: `true`"
    )
    allowLoadingIframes: Optional[bool] = Field(None, description="Default: `false`")
    linguistsMayEditSource: Optional[bool] = Field(None, description="Default: `true`")
    linguistsMayEditTagContent: Optional[bool] = Field(
        None, description="Default: `true`"
    )
    linguistsMayDownloadLqaReport: Optional[bool] = Field(
        None, description="Default: `true`"
    )
    usernamesDisplayedInLqaReport: Optional[bool] = Field(
        None, description="Default: `true`"
    )
    userMaySetInstantQA: Optional[bool] = Field(None, description="Default: `true`")
    triggerWebhooks: Optional[bool] = Field(None, description="Default: `true`")
    vendors: Optional[VendorSecuritySettingsDto] = None
    allowedDomains: Optional[List[str]] = None


class WorkflowStepSettingsEditDto(BaseModel):
    workflowStep: Optional[IdReference] = None
    assignedTo: Optional[List[ProjectTemplateWorkflowSettingsAssignedToDto]] = None
    notifyProvider: Optional[ProjectTemplateNotifyProviderDto] = None
    lqaProfile: Optional[UidReference] = None


class ProjectTemplateReference(BaseModel):
    templateName: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    id: Optional[str] = None
    uid: Optional[str] = None
    owner: Optional[UserReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    costCenter: Optional[CostCenterReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    note: Optional[str] = None
    client: Optional[ClientReference] = None


class Type10(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    PreAnalyseTarget = "PreAnalyseTarget"
    Compare = "Compare"


class AbstractAnalyseSettingsDto(BaseModel):
    type: Optional[Type10] = Field(
        None, description="Response differs based on analyse type"
    )
    includeConfirmedSegments: Optional[bool] = Field(None, description="Default: false")
    includeNumbers: Optional[bool] = Field(None, description="Default: false")
    includeLockedSegments: Optional[bool] = Field(None, description="Default: false")
    countSourceUnits: Optional[bool] = Field(None, description="Default: false")
    includeTransMemory: Optional[bool] = Field(None, description="Default: false")
    namingPattern: Optional[str] = None
    analyzeByLanguage: Optional[bool] = Field(None, description="Default: false")
    analyzeByProvider: Optional[bool] = Field(None, description="Default: false")
    allowAutomaticPostAnalysis: Optional[bool] = Field(
        None,
        description="If automatic post analysis should be created after update source. Default: false",
    )


class PostAnalyse(AbstractAnalyseSettingsDto):
    transMemoryPostEditing: Optional[bool] = Field(None, description="Default: false")
    nonTranslatablePostEditing: Optional[bool] = Field(
        None, description="Default: false"
    )
    machineTranslatePostEditing: Optional[bool] = Field(
        None, description="Default: false"
    )


class PreAnalyse(AbstractAnalyseSettingsDto):
    includeFuzzyRepetitions: Optional[bool] = Field(None, description="Default: false")
    separateFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    includeNonTranslatables: Optional[bool] = Field(None, description="Default: false")
    includeMachineTranslationMatches: Optional[bool] = Field(
        None, description="Default: false"
    )


class PreAnalyseTargetCompare(AbstractAnalyseSettingsDto):
    transMemoryPostEditing: Optional[bool] = Field(None, description="Default: false")
    nonTranslatablePostEditing: Optional[bool] = Field(
        None, description="Default: false"
    )
    machineTranslatePostEditing: Optional[bool] = Field(
        None, description="Default: false"
    )
    includeFuzzyRepetitions: Optional[bool] = Field(None, description="Default: false")
    separateFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    includeNonTranslatables: Optional[bool] = Field(None, description="Default: false")
    includeMachineTranslationMatches: Optional[bool] = Field(
        None, description="Default: false"
    )


class Type11(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    PreAnalyseTarget = "PreAnalyseTarget"
    Compare = "Compare"


class EditAnalyseSettingsDto(BaseModel):
    type: Optional[Type11] = None
    includeFuzzyRepetitions: Optional[bool] = Field(None, description="Default: false")
    separateFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    includeNonTranslatables: Optional[bool] = Field(None, description="Default: false")
    includeMachineTranslationMatches: Optional[bool] = Field(
        None, description="Default: false"
    )
    includeConfirmedSegments: Optional[bool] = Field(None, description="Default: false")
    includeNumbers: Optional[bool] = Field(None, description="Default: false")
    includeLockedSegments: Optional[bool] = Field(None, description="Default: false")
    transMemoryPostEditing: Optional[bool] = Field(None, description="Default: false")
    nonTranslatablePostEditing: Optional[bool] = Field(
        None, description="Default: false"
    )
    machineTranslatePostEditing: Optional[bool] = Field(
        None, description="Default: false"
    )
    countSourceUnits: Optional[bool] = Field(None, description="Default: false")
    includeTransMemory: Optional[bool] = Field(None, description="Default: false")
    namingPattern: Optional[constr(min_length=0, max_length=255)] = None
    analyzeByLanguage: Optional[bool] = Field(
        None, description="Mutually exclusive with analyzeByProvider. Default: false"
    )
    analyzeByProvider: Optional[bool] = Field(
        None, description="Mutually exclusive with analyzeByLanguage. Default: true"
    )
    allowAutomaticPostAnalysis: Optional[bool] = Field(
        None, description="Default: false"
    )


class SetProjectTemplateTermBaseDto(BaseModel):
    readTermBases: Optional[List[IdReference]] = None
    writeTermBase: Optional[IdReference] = None
    qualityAssuranceTermBases: Optional[List[IdReference]] = None
    targetLang: Optional[str] = None
    workflowStep: Optional[IdReference] = None


class ProjectTermBaseDto(BaseModel):
    targetLocale: Optional[str] = None
    workflowStep: Optional[WorkflowStepReference] = None
    readMode: Optional[bool] = None
    writeMode: Optional[bool] = None
    termBase: Optional[TermBaseDto] = None
    qualityAssurance: Optional[bool] = None


class ProjectTermBaseListDto(BaseModel):
    termBases: Optional[List[ProjectTermBaseDto]] = None


class SetTermBaseDto(BaseModel):
    readTermBases: Optional[List[IdReference]] = None
    writeTermBase: Optional[IdReference] = None
    qualityAssuranceTermBases: Optional[List[IdReference]] = None
    targetLang: Optional[str] = None


class PageDtoTermBaseDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[TermBaseDto]] = None


class SearchTMRequestDto(BaseModel):
    segment: str
    workflowLevel: Optional[conint(ge=1, le=15)] = None
    scoreThreshold: Optional[confloat(ge=0.0, le=1.01)] = None
    previousSegment: Optional[str] = None
    nextSegment: Optional[str] = None
    contextKey: Optional[str] = None
    maxSegments: Optional[conint(ge=0, le=5)] = Field(None, description="Default: 5")
    maxSubSegments: Optional[conint(ge=0, le=5)] = Field(None, description="Default: 5")
    tagMetadata: Optional[List[TagMetadataDto]] = None
    targetLangs: List[str] = Field(..., max_items=2147483647, min_items=1)


class EmailQuotesResponseDto(BaseModel):
    recipients: Optional[List[str]] = None


class EmailQuotesRequestDto(BaseModel):
    quotes: List[UidReference]
    subject: str
    body: str
    cc: Optional[str] = None
    bcc: Optional[str] = None


class Type12(Enum):
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    DECIMAL = "DECIMAL"
    INTEGER = "INTEGER"
    DATE_TIME = "DATE_TIME"
    BINARY = "BINARY"
    REFERENCE = "REFERENCE"
    COMPLEX = "COMPLEX"


class Mutability(Enum):
    READ_ONLY = "READ_ONLY"
    READ_WRITE = "READ_WRITE"
    IMMUTABLE = "IMMUTABLE"
    WRITE_ONLY = "WRITE_ONLY"


class Returned(Enum):
    ALWAYS = "ALWAYS"
    NEVER = "NEVER"
    DEFAULT = "DEFAULT"
    REQUEST = "REQUEST"


class Uniqueness(Enum):
    NONE = "NONE"
    SERVER = "SERVER"
    GLOBAL = "GLOBAL"


class Attribute(BaseModel):
    name: Optional[str] = None
    type: Optional[Type12] = None
    subAttributes: Optional[List[Attribute]] = None
    multiValued: Optional[bool] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    caseExact: Optional[bool] = None
    mutability: Optional[Mutability] = None
    returned: Optional[Returned] = None
    uniqueness: Optional[Uniqueness] = None


class ScimResourceSchema(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[List[Attribute]] = None


class AuthSchema(BaseModel):
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    specUrl: Optional[str] = None
    primary: Optional[bool] = None


class Supported(BaseModel):
    supported: Optional[bool] = None


class SchemaExtension(BaseModel):
    schema_: Optional[str] = Field(None, alias="schema")
    required: Optional[bool] = None


class ScimResourceTypeSchema(BaseModel):
    schemas: Optional[List[str]] = None
    id: Optional[str] = None
    name: Optional[str] = None
    endpoint: Optional[str] = None
    description: Optional[str] = None
    schema_: Optional[str] = Field(None, alias="schema")
    schemaExtensions: Optional[List[SchemaExtension]] = None


class Email(BaseModel):
    value: Optional[str] = None
    type: Optional[str] = None
    primary: Optional[bool] = Field(None, description="Default: false")


class Name2(BaseModel):
    givenName: str
    familyName: str


class ScimMeta(BaseModel):
    created: Optional[datetime] = None
    location: Optional[str] = None


class ScimUserCoreDto(BaseModel):
    id: Optional[str] = None
    userName: str
    name: Name2
    active: Optional[bool] = Field(None, description="Default: true")
    emails: List[Email] = Field(..., max_items=2147483647, min_items=1)
    meta: Optional[ScimMeta] = None


class SegmentationRuleDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: str
    locale: Optional[str] = None
    primary: Optional[bool] = Field(None, description="Default: false")
    filename: str
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = Field(None, description="created by user")


class EditSegmentationRuleDto(BaseModel):
    name: constr(min_length=0, max_length=255)
    primary: Optional[bool] = Field(None, description="Default: false")


class SegmentationRuleReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: str
    locale: Optional[str] = None
    primary: Optional[bool] = Field(None, description="Default: false")
    filename: str
    dateCreated: Optional[datetime] = None


class MisspelledWord(BaseModel):
    word: Optional[str] = None
    offset: Optional[int] = None


class SpellCheckRequestDto(BaseModel):
    lang: str
    texts: List[str]
    referenceTexts: Optional[List[str]] = None
    zeroLengthSeparator: Optional[str] = None


class DictionaryItemDto(BaseModel):
    lang: str
    word: str


class Suggestion(BaseModel):
    text: Optional[str] = None


class SuggestRequestDto(BaseModel):
    lang: str
    words: List[str]
    referenceTexts: Optional[List[str]] = None


class SubDomainDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[UserReference] = None


class SubDomainEditDto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None


class TermBaseEditDto(BaseModel):
    name: constr(min_length=0, max_length=255)
    langs: List[str] = Field(..., max_items=2147483647, min_items=1)
    client: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    owner: Optional[IdReference] = Field(
        None, description="Owner of the TM must be Admin or PM"
    )
    note: Optional[constr(min_length=0, max_length=4096)] = None


class ImportTermBaseResponseDto(BaseModel):
    langs: Optional[List[str]] = None
    createdTermsCount: Optional[int] = None
    updatedTermsCount: Optional[int] = None


class ConceptWithMetadataDto(BaseModel):
    id: Optional[str] = None
    domain: Optional[DomainReference] = None
    subdomains: Optional[List[SubDomainReference]] = None
    url: Optional[str] = None
    definition: Optional[str] = None
    conceptNote: Optional[str] = None


class ConceptEditDto(BaseModel):
    domain: Optional[UidReference] = None
    subdomains: Optional[List[UidReference]] = None
    definition: Optional[str] = None
    url: Optional[str] = None
    conceptNote: Optional[str] = None


class Status18(Enum):
    New = "New"
    Approved = "Approved"


class TermType1(Enum):
    FULL_FORM = "FULL_FORM"
    SHORT_FORM = "SHORT_FORM"
    ACRONYM = "ACRONYM"
    ABBREVIATION = "ABBREVIATION"
    PHRASE = "PHRASE"
    VARIANT = "VARIANT"


class PartOfSpeech1(Enum):
    ADJECTIVE = "ADJECTIVE"
    NOUN = "NOUN"
    VERB = "VERB"
    ADVERB = "ADVERB"


class Gender1(Enum):
    MASCULINE = "MASCULINE"
    FEMININE = "FEMININE"
    NEUTRAL = "NEUTRAL"


class Number2(Enum):
    SINGULAR = "SINGULAR"
    PLURAL = "PLURAL"
    UNCOUNTABLE = "UNCOUNTABLE"


class TermCreateDto(BaseModel):
    text: str
    lang: str
    caseSensitive: Optional[bool] = Field(None, description="Default: false")
    exactMatch: Optional[bool] = Field(None, description="Default: false")
    forbidden: Optional[bool] = Field(None, description="Default: false")
    preferred: Optional[bool] = Field(None, description="Default: false")
    status: Optional[Status18] = None
    conceptId: Optional[str] = None
    usage: Optional[str] = None
    note: Optional[str] = None
    shortTranslation: Optional[str] = None
    termType: Optional[TermType1] = None
    partOfSpeech: Optional[PartOfSpeech1] = None
    gender: Optional[Gender1] = None
    number: Optional[Number2] = None


class Status19(Enum):
    New = "New"
    Approved = "Approved"


class TermType2(Enum):
    FULL_FORM = "FULL_FORM"
    SHORT_FORM = "SHORT_FORM"
    ACRONYM = "ACRONYM"
    ABBREVIATION = "ABBREVIATION"
    PHRASE = "PHRASE"
    VARIANT = "VARIANT"


class PartOfSpeech2(Enum):
    ADJECTIVE = "ADJECTIVE"
    NOUN = "NOUN"
    VERB = "VERB"
    ADVERB = "ADVERB"


class Gender2(Enum):
    MASCULINE = "MASCULINE"
    FEMININE = "FEMININE"
    NEUTRAL = "NEUTRAL"


class Number3(Enum):
    SINGULAR = "SINGULAR"
    PLURAL = "PLURAL"
    UNCOUNTABLE = "UNCOUNTABLE"


class TermEditDto(BaseModel):
    text: str
    lang: Optional[str] = None
    caseSensitive: Optional[bool] = Field(None, description="Default: false")
    exactMatch: Optional[bool] = Field(None, description="Default: false")
    forbidden: Optional[bool] = Field(None, description="Default: false")
    preferred: Optional[bool] = Field(None, description="Default: false")
    status: Optional[Status19] = None
    usage: Optional[str] = None
    note: Optional[str] = None
    shortTranslation: Optional[str] = None
    termType: Optional[TermType2] = None
    partOfSpeech: Optional[PartOfSpeech2] = None
    gender: Optional[Gender2] = None
    number: Optional[Number3] = None


class ConceptListReference(BaseModel):
    concepts: List[IdReference] = Field(..., max_items=100, min_items=1)


class ConceptDto(BaseModel):
    id: Optional[str] = None
    writable: Optional[bool] = None
    terms: Optional[List[List[TermDto]]] = None


class BrowseResponseListDto(BaseModel):
    searchResults: Optional[List[ConceptDto]] = None


class BrowseRequestDto(BaseModel):
    queryLang: Optional[str] = None
    query: Optional[str] = None
    status: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[conint(ge=1, le=50)] = None


class Status20(Enum):
    New = "New"
    Approved = "Approved"


class TermBaseSearchRequestDto(BaseModel):
    targetLangs: List[str]
    sourceLang: str
    query: str
    status: Optional[Status20] = None


class MetadataTbDto(BaseModel):
    termsCount: Optional[int] = None
    metadataByLanguage: Optional[Dict[str, int]] = None


class SearchRequestDto(BaseModel):
    query: str
    sourceLang: str
    targetLangs: Optional[List[str]] = None
    previousSegment: Optional[str] = None
    nextSegment: Optional[str] = None
    tagMetadata: Optional[List[TagMetadataDto]] = None
    trimQuery: Optional[bool] = Field(
        None,
        description="Remove leading and trailing whitespace from query. Default: true",
    )
    phraseQuery: Optional[bool] = Field(
        None, description="Return both wildcard and exact search results. Default: true"
    )


class OutputFormat(Enum):
    TXT = "TXT"
    TSV = "TSV"


class CleanedTransMemoriesDto(BaseModel):
    uids: List[str]
    outputFormat: Optional[OutputFormat] = None
    preserveRatio: Optional[confloat(le=1.0, gt=0.0)] = None
    targetLangs: Optional[List[str]] = None


class TransMemoryEditDto(BaseModel):
    name: constr(min_length=0, max_length=255)
    targetLangs: List[str] = Field(
        ..., description="New target languages to add. No languages can be removed"
    )
    client: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    owner: Optional[IdReference] = Field(
        None, description="Owner of the TM must be Admin or PM"
    )
    note: Optional[constr(min_length=0, max_length=4096)] = None


class TransMemoryCreateDto(BaseModel):
    name: constr(min_length=0, max_length=255)
    sourceLang: str
    targetLangs: List[str]
    client: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    note: Optional[constr(min_length=0, max_length=4096)] = None


class TargetLanguageDto(BaseModel):
    language: str


class SegmentDto(BaseModel):
    targetLang: str
    sourceSegment: str
    targetSegment: str
    previousSourceSegment: Optional[str] = None
    nextSourceSegment: Optional[str] = None
    sourceTagMetadata: Optional[List[TagMetadataDto]] = None
    targetTagMetadata: Optional[List[TagMetadataDto]] = None


class LanguageMetadata1(BaseModel):
    segmentsCount: Optional[int] = None


class TranslationDto(BaseModel):
    lang: str
    text: str


class WildCardSearchRequestDto(BaseModel):
    query: Optional[str] = None
    sourceLang: str
    targetLangs: Optional[List[str]] = None
    count: Optional[conint(ge=1, le=50)] = None
    offset: Optional[int] = None
    sourceLangs: Optional[List[str]] = None


class Query(BaseModel):
    query: Optional[str] = None
    lang: Optional[str] = None


class ExportByQueryDto(BaseModel):
    exportTargetLangs: List[str]
    queries: List[str]
    queryLangs: List[str]
    createdAtMin: Optional[datetime] = None
    createdAtMax: Optional[datetime] = None
    modifiedAtMin: Optional[datetime] = None
    modifiedAtMax: Optional[datetime] = None
    createdBy: Optional[IdReference] = None
    modifiedBy: Optional[IdReference] = None
    filename: Optional[str] = None
    project: Optional[UidReference] = None
    callbackUrl: Optional[str] = None


class TranslationRequestDto(BaseModel):
    sourceTexts: List[str] = Field(..., max_items=2147483647, min_items=1)


class TranslationPriceDto(BaseModel):
    workflowStep: Optional[WorkflowStepDto] = None
    price: Optional[float] = None


class BillingUnit1(Enum):
    Character = "Character"
    Word = "Word"
    Page = "Page"
    Hour = "Hour"


class TranslationPriceSetDto(BaseModel):
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    minimumPrice: Optional[float] = None
    prices: Optional[List[TranslationPriceDto]] = None


class BillingUnit2(Enum):
    Word = "Word"
    Page = "Page"
    Character = "Character"
    Hour = "Hour"


class TranslationPriceListCreateDto(BaseModel):
    name: str
    currencyCode: str
    billingUnit: Optional[BillingUnit2] = Field(None, description="Default: Word")


class TranslationPriceSetListDto(BaseModel):
    priceSets: Optional[List[TranslationPriceSetDto]] = None


class TranslationPriceSetCreateDto(BaseModel):
    sourceLanguages: List[str] = Field(..., max_items=100, min_items=1)
    targetLanguages: List[str] = Field(..., max_items=100, min_items=1)


class TranslationPriceSetBulkDeleteDto(BaseModel):
    sourceLanguages: Optional[List[str]] = None
    targetLanguages: Optional[List[str]] = None


class PageDtoTranslationPriceSetDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[TranslationPriceSetDto]] = None


class TranslationPriceSetBulkMinimumPricesDto(BaseModel):
    sourceLanguages: Optional[List[str]] = None
    targetLanguages: Optional[List[str]] = None
    minimumPrice: Optional[float] = None


class TranslationPriceSetBulkPricesDto(BaseModel):
    sourceLanguages: Optional[List[str]] = None
    targetLanguages: Optional[List[str]] = None
    price: Optional[float] = None
    workflowSteps: Optional[List[IdReference]] = Field(None, max_items=15, min_items=0)


class PageDtoString(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[str]] = None


class LastLoginDto(BaseModel):
    user: Optional[UserReference] = None
    lastLoginDate: Optional[datetime] = None


class PageDtoLastLoginDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[LastLoginDto]] = None


class Status21(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Role3(Enum):
    SYS_ADMIN = "SYS_ADMIN"
    SYS_ADMIN_READ = "SYS_ADMIN_READ"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LINGUIST = "LINGUIST"
    GUEST = "GUEST"
    SUBMITTER = "SUBMITTER"


class UserDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    userName: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    dateCreated: Optional[datetime] = None
    dateDeleted: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    role: Optional[Role3] = None
    timezone: Optional[str] = None
    note: Optional[str] = None
    terminologist: Optional[bool] = None
    sourceLangs: Optional[List[str]] = None
    targetLangs: Optional[List[str]] = None
    active: Optional[bool] = None
    priceList: Optional[PriceListReference] = None
    netRateScheme: Optional[DiscountSchemeReference] = None


class UserStatisticsDto(BaseModel):
    date: Optional[datetime] = None
    ipAddress: Optional[str] = None
    ipCountry: Optional[str] = None
    userAgent: Optional[str] = None


class UserStatisticsListDto(BaseModel):
    userStatistics: List[UserStatisticsDto]


class PageDtoUserDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[UserDto]] = None


class PageDtoWorkflowStepReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[WorkflowStepReference]] = None


class UserPasswordEditDto(BaseModel):
    password: constr(min_length=8, max_length=255)


class VendorDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    vendorToken: Optional[str] = None
    priceList: Optional[PriceListReference] = None
    netRateScheme: Optional[DiscountSchemeReference] = None
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    clients: Optional[List[ClientReference]] = None
    domains: Optional[List[DomainReference]] = None
    subDomains: Optional[List[SubDomainReference]] = None
    workflowSteps: Optional[List[WorkflowStepReference]] = None


class CreateVendorDto(BaseModel):
    vendorToken: str
    netRateScheme: Optional[UidReference] = None
    priceList: Optional[UidReference] = None
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    clients: Optional[List[UidReference]] = None
    domains: Optional[List[UidReference]] = None
    subDomains: Optional[List[UidReference]] = None
    workflowSteps: Optional[List[UidReference]] = None


class PageDtoVendorDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[VendorDto]] = None


class TriggerEvent(Enum):
    JOB_STATUS_CHANGED = "JOB_STATUS_CHANGED"
    JOB_CREATED = "JOB_CREATED"
    JOB_DELETED = "JOB_DELETED"
    JOB_ASSIGNED = "JOB_ASSIGNED"
    JOB_DUE_DATE_CHANGED = "JOB_DUE_DATE_CHANGED"
    JOB_UPDATED = "JOB_UPDATED"
    JOB_TARGET_UPDATED = "JOB_TARGET_UPDATED"
    JOB_EXPORTED = "JOB_EXPORTED"
    JOB_UNEXPORTED = "JOB_UNEXPORTED"
    PROJECT_CREATED = "PROJECT_CREATED"
    PROJECT_DELETED = "PROJECT_DELETED"
    PROJECT_STATUS_CHANGED = "PROJECT_STATUS_CHANGED"
    PROJECT_DUE_DATE_CHANGED = "PROJECT_DUE_DATE_CHANGED"
    SHARED_PROJECT_ASSIGNED = "SHARED_PROJECT_ASSIGNED"
    PROJECT_METADATA_UPDATED = "PROJECT_METADATA_UPDATED"
    PRE_TRANSLATION_FINISHED = "PRE_TRANSLATION_FINISHED"
    ANALYSIS_CREATED = "ANALYSIS_CREATED"
    CONTINUOUS_JOB_UPDATED = "CONTINUOUS_JOB_UPDATED"
    PROJECT_TEMPLATE_CREATED = "PROJECT_TEMPLATE_CREATED"
    PROJECT_TEMPLATE_UPDATED = "PROJECT_TEMPLATE_UPDATED"
    PROJECT_TEMPLATE_DELETED = "PROJECT_TEMPLATE_DELETED"


class WebhookCallDto(BaseModel):
    uid: Optional[str] = None
    parentUid: Optional[str] = None
    webhookSettings: Optional[UidReference] = None
    createdAt: Optional[datetime] = None
    url: Optional[str] = None
    forced: Optional[bool] = None
    lastForcedAt: Optional[datetime] = None
    body: Optional[str] = None
    triggerEvent: Optional[TriggerEvent] = None
    retryAttempt: Optional[int] = None
    statusCode: Optional[int] = None
    errorMessage: Optional[str] = None


class ReplayRequestDto(BaseModel):
    webhookCalls: Optional[List[UidReference]] = None


class CreateWorkflowStepDto(BaseModel):
    name: constr(min_length=1, max_length=255) = Field(
        ..., description="Name of the lqa workflow step"
    )
    order: Optional[int] = Field(None, description="Order value")
    lqaEnabled: Optional[bool] = Field(None, description="Default: false")
    abbr: constr(min_length=1, max_length=3) = Field(..., description="Abbreviation")


class EditWorkflowStepDto(BaseModel):
    name: constr(min_length=1, max_length=255) = Field(
        ..., description="Name of the lqa workflow step"
    )
    order: Optional[int] = Field(None, description="Order value")
    lqaEnabled: Optional[bool] = Field(None, description="Default: false")
    abbr: constr(min_length=1, max_length=3) = Field(..., description="Abbreviation")


class PageDtoWorkflowStepDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[WorkflowStepDto]] = None


class Type13(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    PreAnalyseTarget = "PreAnalyseTarget"
    Compare = "Compare"
    PreAnalyseProvider = "PreAnalyseProvider"


class MatchCountsNTDto(BaseModel):
    match100: Optional[CountsDto] = None
    match95: Optional[CountsDto] = None
    match85: Optional[CountsDto] = None
    match75: Optional[CountsDto] = None
    match50: Optional[CountsDto] = None
    match0: Optional[CountsDto] = None


class Action2(Enum):
    PRE_ANALYSE = "PRE_ANALYSE"
    POST_ANALYSE = "POST_ANALYSE"
    COMPARE_ANALYSE = "COMPARE_ANALYSE"
    PARENT_ANALYSE = "PARENT_ANALYSE"
    PRE_TRANSLATE = "PRE_TRANSLATE"
    ASYNC_TRANSLATE = "ASYNC_TRANSLATE"
    IMPORT_JOB = "IMPORT_JOB"
    IMPORT_FILE = "IMPORT_FILE"
    ALIGN = "ALIGN"
    EXPORT_TMX_BY_QUERY = "EXPORT_TMX_BY_QUERY"
    EXPORT_TMX = "EXPORT_TMX"
    IMPORT_TMX = "IMPORT_TMX"
    INSERT_INTO_TM = "INSERT_INTO_TM"
    DELETE_TM = "DELETE_TM"
    CLEAR_TM = "CLEAR_TM"
    QA = "QA"
    QA_V3 = "QA_V3"
    UPDATE_CONTINUOUS_JOB = "UPDATE_CONTINUOUS_JOB"
    UPDATE_SOURCE = "UPDATE_SOURCE"
    UPDATE_TARGET = "UPDATE_TARGET"
    EXTRACT_CLEANED_TMS = "EXTRACT_CLEANED_TMS"
    GLOSSARY_PUT = "GLOSSARY_PUT"
    GLOSSARY_DELETE = "GLOSSARY_DELETE"
    CREATE_PROJECT = "CREATE_PROJECT"
    EXPORT_COMPLETE_FILE = "EXPORT_COMPLETE_FILE"


class ErrorDetailDtoV2(BaseModel):
    code: Optional[str] = Field(None, description="Code, e.g. NOT_FOUND.")
    args: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description='Related arguments, e.g. number => "hello world"'
    )
    message: Optional[str] = Field(None, description="Optional human-readable message.")


class Type14(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    Compare = "Compare"


class CreateAnalyseAsyncV2Dto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=50000, min_items=1)
    type: Optional[Type14] = Field(None, description="default: PreAnalyse")
    includeFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    separateFuzzyRepetitions: Optional[bool] = Field(None, description="Default: true")
    includeConfirmedSegments: Optional[bool] = Field(None, description="Default: true")
    includeNumbers: Optional[bool] = Field(None, description="Default: true")
    includeLockedSegments: Optional[bool] = Field(None, description="Default: true")
    countSourceUnits: Optional[bool] = Field(None, description="Default: true")
    includeTransMemory: Optional[bool] = Field(
        None, description="Default: true. Works only for type=PreAnalyse."
    )
    includeNonTranslatables: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PreAnalyse."
    )
    includeMachineTranslationMatches: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PreAnalyse."
    )
    transMemoryPostEditing: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PostAnalyse."
    )
    nonTranslatablePostEditing: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PostAnalyse."
    )
    machineTranslatePostEditing: Optional[bool] = Field(
        None, description="Default: false. Works only for type=PostAnalyse."
    )
    name: Optional[constr(min_length=0, max_length=255)] = None
    netRateScheme: Optional[IdReference] = None
    compareWorkflowLevel: Optional[conint(ge=1, le=15)] = Field(
        None, description="Required for type=Compare"
    )
    useProjectAnalysisSettings: Optional[bool] = Field(
        None,
        description="Default: false. Use default project settings. Will be overwritten with setting sent\n        in the API call.",
    )
    callbackUrl: Optional[str] = None
    provider: Optional[ProviderReference] = None


class EditAnalyseV2Dto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None
    provider: Optional[ProviderReference] = None
    netRateScheme: Optional[UidReference] = None


class BulkEditAnalyseV2Dto(BaseModel):
    analyses: List[IdReference] = Field(..., max_items=100, min_items=1)
    name: Optional[constr(min_length=0, max_length=255)] = None
    provider: Optional[ProviderReference] = None
    netRateScheme: Optional[UidReference] = None


class Action3(Enum):
    GUI_UPLOAD = "GUI_UPLOAD"
    GUI_DOWNLOAD = "GUI_DOWNLOAD"
    GUI_REIMPORT = "GUI_REIMPORT"
    CJ_UPLOAD = "CJ_UPLOAD"
    CJ_DOWNLOAD = "CJ_DOWNLOAD"
    APC_UPLOAD = "APC_UPLOAD"
    APC_DOWNLOAD = "APC_DOWNLOAD"
    API_UPLOAD = "API_UPLOAD"
    API_DOWNLOAD = "API_DOWNLOAD"
    SUBMITTER_PORTAL_DOWNLOAD = "SUBMITTER_PORTAL_DOWNLOAD"


class AsyncFileOpResponseDto(BaseModel):
    id: Optional[str] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    fileName: Optional[str] = None
    action: Optional[Action3] = None


class GetFileRequestParamsDto(BaseModel):
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    callbackUrl: str = Field(
        ..., example='{"callbackUrl": "https://www.yourdomain.com/callback_endpoint"}'
    )


class Response(BaseModel):
    context: Optional[Dict[str, Dict[str, Any]]] = None
    done: Optional[bool] = None
    cancelled: Optional[bool] = None


class WorkflowChangesDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)


class AbstractProjectDtoV2(BaseModel):
    uid: Optional[str] = None
    internalId: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    dateCreated: Optional[datetime] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    owner: Optional[UserReference] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = Field(None, unique_items=True)
    references: Optional[List[ReferenceFileReference]] = None
    mtSettingsPerLanguageList: Optional[List[MTSettingsPerLanguageReference]] = None
    userRole: Optional[str] = Field(
        None, description="Response differs based on user's role"
    )


class Status22(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class LinguistV2(AbstractProjectDtoV2):
    pass


class ProgressDtoV2(BaseModel):
    totalCount: Optional[int] = None
    finishedCount: Optional[int] = None
    overdueCount: Optional[int] = None


class CreateProjectFromTemplateV2Dto(BaseModel):
    name: constr(min_length=0, max_length=255)
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    workflowSteps: Optional[List[IdReference]] = None
    dateDue: Optional[datetime] = None
    note: Optional[str] = None
    client: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    costCenter: Optional[IdReference] = None


class CreateProjectFromTemplateAsyncV2Dto(BaseModel):
    name: constr(min_length=0, max_length=255)
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    workflowSteps: Optional[List[IdReference]] = None
    dateDue: Optional[datetime] = None
    note: Optional[str] = None
    client: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    costCenter: Optional[IdReference] = None
    callbackUrl: Optional[str] = None


class LqaProfilesForWsV2Dto(BaseModel):
    workflowStep: Optional[IdReference] = None
    lqaProfile: Optional[UidReference] = None


class CustomFieldInstanceApiDto(BaseModel):
    customField: Optional[UidReference] = None
    selectedOptions: Optional[List[UidReference]] = None
    value: Optional[constr(min_length=0, max_length=4096)] = None


class Status23(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    ACCEPTED_BY_VENDOR = "ACCEPTED_BY_VENDOR"
    DECLINED_BY_VENDOR = "DECLINED_BY_VENDOR"
    COMPLETED_BY_VENDOR = "COMPLETED_BY_VENDOR"
    CANCELLED = "CANCELLED"


class EditProjectV2Dto(BaseModel):
    name: constr(min_length=0, max_length=255)
    status: Optional[Status23] = None
    client: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    owner: Optional[IdReference] = Field(None, description="Owner must be Admin or PM")
    purchaseOrder: Optional[constr(min_length=0, max_length=255)] = None
    dateDue: Optional[datetime] = None
    note: Optional[constr(min_length=0, max_length=4096)] = None
    fileHandover: Optional[bool] = Field(None, description="Default: false")
    lqaProfiles: Optional[List[LqaProfilesForWsV2Dto]] = Field(
        None, description="Lqa profiles that will be added to workflow steps"
    )
    archived: Optional[bool] = Field(None, description="Default: false")
    customFields: Optional[List[CustomFieldInstanceApiDto]] = Field(
        None, description="Custom fields for project"
    )


class ProviderListDtoV2(BaseModel):
    providers: Optional[Providers] = None


class SubstituteDtoV2(BaseModel):
    source: constr(min_length=1, max_length=1)
    target: constr(min_length=1, max_length=1)


class JobMachineTranslationSettingsDto(BaseModel):
    useMachineTranslation: Optional[bool] = Field(
        None, description="Pre-translate from machine translation. Default: true"
    )
    lock100PercentMatches: Optional[bool] = Field(
        None,
        description="Lock section: 100% machine translation matches. Default: false",
    )
    confirm100PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 100% translation machine matches. Default: false",
    )
    useAltTransOnly: Optional[bool] = Field(
        None,
        description="Do not put machine translations to target and use alt-trans fields (alt-trans in mxlf).\nDefault: false",
    )


class JobNonTranslatableSettingsDto(BaseModel):
    preTranslateNonTranslatables: Optional[bool] = Field(
        None, description="Pre-translate non-translatables. Default: true"
    )
    confirm100PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 100% non-translatable matches. Default: false",
    )
    lock100PercentMatches: Optional[bool] = Field(
        None, description="Lock section: 100% non-translatable matches. Default: false"
    )


class JobTranslationMemorySettingsDto(BaseModel):
    useTranslationMemory: Optional[bool] = Field(
        None, description="Pre-translate from translation memory. Default: true"
    )
    translationMemoryThreshold: Optional[confloat(ge=0.0, le=1.01)] = Field(
        None, description="Pre-translation threshold percent. Default: 0.7"
    )
    confirm100PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 100% translation memory matches. Default: false",
    )
    confirm101PercentMatches: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: 101% translation memory matches. Default: false",
    )
    lock100PercentMatches: Optional[bool] = Field(
        None,
        description="Lock section: 100% translation memory matches. Default: false",
    )
    lock101PercentMatches: Optional[bool] = Field(
        None,
        description="Lock section: 101% translation memory matches. Default: false",
    )


class PreTranslateJobSettingsDto(BaseModel):
    autoPropagateRepetitions: Optional[bool] = Field(
        None, description="Propagate repetitions. Default: false"
    )
    confirmRepetitions: Optional[bool] = Field(
        None,
        description="Set segment status to confirmed for: Repetitions. Default: false",
    )
    setJobStatusCompleted: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed: Set job to completed once pre-translated. Default: false",
    )
    setJobStatusCompletedWhenConfirmed: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed when all segments confirmed:\nSet job to completed once pre-translated and all segments are confirmed. Default: false",
    )
    setProjectStatusCompleted: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed: Set project to completed once all jobs pre-translated.\n        Default: false",
    )
    overwriteExistingTranslations: Optional[bool] = Field(
        None,
        description="Overwrite existing translations in target segments. Default: false",
    )
    translationMemorySettings: Optional[JobTranslationMemorySettingsDto] = None
    machineTranslationSettings: Optional[JobMachineTranslationSettingsDto] = None
    nonTranslatableSettings: Optional[JobNonTranslatableSettingsDto] = None


class SegmentFilter(Enum):
    LOCKED = "LOCKED"
    NOT_LOCKED = "NOT_LOCKED"


class PreTranslateJobsV2Dto(BaseModel):
    jobs: List[UidReference] = Field(
        ..., description="Jobs to be pre-translated", max_items=100, min_items=1
    )
    segmentFilters: Optional[List[SegmentFilter]] = None
    useProjectPreTranslateSettings: Optional[bool] = Field(
        None,
        description="If pre-translate settings from project should be used.\nIf true, preTranslateSettings values are ignored. Default: false",
    )
    callbackUrl: Optional[str] = None
    preTranslateSettings: Optional[PreTranslateJobSettingsDto] = Field(
        None,
        description="Pre-translate settings, used if useProjectPreTranslateSettings is false",
    )


class TranslationSegmentsReferenceV2(BaseModel):
    confirmed: Optional[bool] = Field(
        None,
        description="Remove confirmed (true), unconfirmed (false) or both segments (null). Default: null",
    )
    locked: Optional[bool] = Field(
        None,
        description="Remove locked (true), unlocked (false) or both segments (null). Default: false",
    )


class EnabledCheckContextDtoV2(BaseModel):
    moraviaProfileId: Optional[str] = None


class EnabledCheckDtoV2(BaseModel):
    checkerType: Optional[str] = None
    context: Optional[EnabledCheckContextDtoV2] = None


class QualityAssuranceChecksDtoV2(BaseModel):
    forbiddenStrings: Optional[List[str]] = None
    enabledChecks: Optional[List[EnabledCheckDtoV2]] = Field(
        None,
        description="enabledChecks",
        example='\n   [\n      {\n         "checkerType":"EmptyTranslation",\n         "ignorable":false\n      },\n      {\n         "checkerType":"TrailingPunctuation",\n         "ignorable":false\n      },\n      {\n         "checkerType":"Formatting",\n         "ignorable":false\n      },\n      {\n         "checkerType":"JoinTags",\n         "ignorable":false\n      },\n      {\n         "checkerType":"MissingNumbers",\n         "ignorable":false\n      },\n      {\n         "checkerType":"MultipleSpaces",\n         "ignorable":false\n      },\n      {\n         "checkerType":"NonConformingTerm",\n         "ignorable":false\n      },\n      {\n         "checkerType":"NotConfirmed",\n         "ignorable":false\n      },\n      {\n         "checkerType":"TranslationLength",\n         "ignorable":false\n      },\n      {\n         "checkerType": "AbsoluteLength",\n         "ignorable": false\n      },\n      {\n         "checkerType": "RelativeLength",\n         "ignorable": false\n      },\n      {\n         "checkerType":"EmptyPairTags",\n         "ignorable":false\n      },\n      {\n         "checkerType":"InconsistentTranslationTargetSource",\n         "ignorable":true\n      },\n      {\n         "checkerType":"InconsistentTranslationSourceTarget",\n         "ignorable":true\n      },\n      {\n         "checkerType":"ForbiddenString",\n         "ignorable":false\n      },\n      {\n         "checkerType":"SpellCheck",\n         "ignorable":false\n      },\n      {\n         "checkerType":"RepeatedWords",\n         "ignorable":false\n      },\n      {\n         "checkerType":"InconsistentTagContent",\n         "ignorable":false\n      },\n      {\n         "checkerType":"EmptyTagContent",\n         "ignorable":false\n      },\n      {\n         "checkerType":"Malformed",\n         "ignorable":false\n      },\n      {\n         "checkerType":"ForbiddenTerm",\n         "ignorable":false\n      },\n      {\n         "checkerType":"NewerAtLowerLevel",\n         "ignorable":false\n      },\n      {\n         "checkerType":"LeadingAndTrailingSpaces",\n         "ignorable":false\n      },\n      {\n         "checkerType":"TargetSourceIdentical",\n         "ignorable":false\n      },\n      {\n         "checkerType":"SourceOrTargetRegexp"\n      },\n      {\n         "checkerType":"UnmodifiedFuzzyTranslationTM",\n         "ignorable":true\n      },\n      {\n         "checkerType":"UnmodifiedFuzzyTranslationMTNT",\n         "ignorable":true\n      },\n      {\n         "checkerType":"Moravia",\n         "ignorable":false,\n         "context": {"moraviaProfileId": "MoraviaProfileIdValue"}\n      },\n      {\n         "checkerType":"ExtraNumbers",\n         "ignorable":true\n      },\n      {\n         "checkerType":"UnresolvedConversation",\n         "ignorable":false\n      },\n      {\n         "checkerType":"NestedTags",\n         "ignorable":false\n      }\n   ]\n',
    )
    excludeLockedSegments: Optional[bool] = None
    userCanSetInstantQA: Optional[bool] = None
    strictJobStatus: Optional[bool] = None
    regexpRules: Optional[List[RegexpCheckRuleDtoV2]] = None


class WebEditorLinkDtoV2(BaseModel):
    url: Optional[str] = None
    warnings: Optional[List[ErrorDetailDtoV2]] = None


class CreateWebEditorLinkDtoV2(BaseModel):
    jobs: List[UidReference] = Field(
        ...,
        description="Maximum supported number of jobs is 290",
        max_items=2147483647,
        min_items=1,
    )


class TransMemoryDtoV2(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    internalId: Optional[int] = None
    name: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    client: Optional[ClientReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    note: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None


class TransMemoryReferenceDtoV2(BaseModel):
    internalId: Optional[int] = None
    uid: str
    name: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None


class ProjectTemplateTransMemoryV2Dto(BaseModel):
    targetLocale: Optional[str] = None
    workflowStep: Optional[WorkflowStepReferenceV2] = None
    readMode: Optional[bool] = None
    writeMode: Optional[bool] = None
    transMemory: Optional[TransMemoryDtoV2] = None
    penalty: Optional[float] = None
    applyPenaltyTo101Only: Optional[bool] = None
    order: Optional[int] = None


class SetProjectTemplateTransMemoryV2Dto(BaseModel):
    transMemory: UidReference
    readMode: Optional[bool] = Field(None, description="Default: false")
    writeMode: Optional[bool] = Field(
        None,
        description="Can be set only for Translation Memory with read == true.<br/>\n        Max 2 write TMs allowed per project.<br/>\n        Default: false",
    )
    penalty: Optional[confloat(ge=0.0, le=100.0)] = None
    applyPenaltyTo101Only: Optional[bool] = Field(
        None, description="Can be set only for penalty == 1<br/>Default: false"
    )
    order: Optional[int] = None


class Status24(Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    DRAFT = "DRAFT"
    FOR_APPROVAL = "FOR_APPROVAL"
    NEW = "NEW"


class BillingUnit3(Enum):
    Character = "Character"
    Word = "Word"
    Page = "Page"
    Hour = "Hour"


class QuoteType1(Enum):
    BUYER = "BUYER"
    PROVIDER = "PROVIDER"


class QuoteV2Dto(BaseModel):
    id: Optional[int] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    status: Optional[Status24] = None
    currency: Optional[str] = None
    billingUnit: Optional[BillingUnit3] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    totalPrice: Optional[float] = None
    netRateScheme: Optional[NetRateSchemeReference] = None
    priceList: Optional[PriceListReference] = None
    workflowStepList: Optional[List[WorkflowStepReference]] = None
    provider: Optional[ProviderReference] = None
    customerEmail: Optional[str] = None
    quoteType: Optional[QuoteType1] = None
    editable: Optional[bool] = None
    outdated: Optional[bool] = None


class QuoteUnitsDto(BaseModel):
    analyseLanguagePart: IdReference
    value: Optional[confloat(ge=0.0)] = None


class QuoteWorkflowSettingDto(BaseModel):
    workflowStep: IdReference
    units: Optional[List[QuoteUnitsDto]] = Field(None, max_items=100, min_items=0)


class AsyncExportTMDto(BaseModel):
    transMemory: Optional[ObjectReference] = None
    exportTargetLangs: Optional[List[str]] = None


class ExportTMDto(BaseModel):
    exportTargetLangs: Optional[List[str]] = None
    callbackUrl: Optional[str] = None


class Event(Enum):
    JOB_STATUS_CHANGED = "JOB_STATUS_CHANGED"
    JOB_CREATED = "JOB_CREATED"
    JOB_DELETED = "JOB_DELETED"
    JOB_ASSIGNED = "JOB_ASSIGNED"
    JOB_DUE_DATE_CHANGED = "JOB_DUE_DATE_CHANGED"
    JOB_UPDATED = "JOB_UPDATED"
    JOB_TARGET_UPDATED = "JOB_TARGET_UPDATED"
    JOB_EXPORTED = "JOB_EXPORTED"
    JOB_UNEXPORTED = "JOB_UNEXPORTED"
    PROJECT_CREATED = "PROJECT_CREATED"
    PROJECT_DELETED = "PROJECT_DELETED"
    PROJECT_STATUS_CHANGED = "PROJECT_STATUS_CHANGED"
    PROJECT_DUE_DATE_CHANGED = "PROJECT_DUE_DATE_CHANGED"
    SHARED_PROJECT_ASSIGNED = "SHARED_PROJECT_ASSIGNED"
    PROJECT_METADATA_UPDATED = "PROJECT_METADATA_UPDATED"
    PRE_TRANSLATION_FINISHED = "PRE_TRANSLATION_FINISHED"
    ANALYSIS_CREATED = "ANALYSIS_CREATED"
    CONTINUOUS_JOB_UPDATED = "CONTINUOUS_JOB_UPDATED"
    PROJECT_TEMPLATE_CREATED = "PROJECT_TEMPLATE_CREATED"
    PROJECT_TEMPLATE_UPDATED = "PROJECT_TEMPLATE_UPDATED"
    PROJECT_TEMPLATE_DELETED = "PROJECT_TEMPLATE_DELETED"


class Status25(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class WebHookDtoV2(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None
    url: str
    events: Optional[List[Event]] = None
    secretToken: constr(min_length=1, max_length=255)
    hidden: Optional[bool] = Field(None, description="Default: false")
    status: Optional[Status25] = None
    failedAttempts: Optional[int] = None
    created: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    lastModified: Optional[datetime] = None
    lastModifiedBy: Optional[UserReference] = None


class Event1(Enum):
    JOB_STATUS_CHANGED = "JOB_STATUS_CHANGED"
    JOB_CREATED = "JOB_CREATED"
    JOB_DELETED = "JOB_DELETED"
    JOB_ASSIGNED = "JOB_ASSIGNED"
    JOB_DUE_DATE_CHANGED = "JOB_DUE_DATE_CHANGED"
    JOB_UPDATED = "JOB_UPDATED"
    JOB_TARGET_UPDATED = "JOB_TARGET_UPDATED"
    JOB_EXPORTED = "JOB_EXPORTED"
    JOB_UNEXPORTED = "JOB_UNEXPORTED"
    PROJECT_CREATED = "PROJECT_CREATED"
    PROJECT_DELETED = "PROJECT_DELETED"
    PROJECT_STATUS_CHANGED = "PROJECT_STATUS_CHANGED"
    PROJECT_DUE_DATE_CHANGED = "PROJECT_DUE_DATE_CHANGED"
    SHARED_PROJECT_ASSIGNED = "SHARED_PROJECT_ASSIGNED"
    PROJECT_METADATA_UPDATED = "PROJECT_METADATA_UPDATED"
    PRE_TRANSLATION_FINISHED = "PRE_TRANSLATION_FINISHED"
    ANALYSIS_CREATED = "ANALYSIS_CREATED"
    CONTINUOUS_JOB_UPDATED = "CONTINUOUS_JOB_UPDATED"
    PROJECT_TEMPLATE_CREATED = "PROJECT_TEMPLATE_CREATED"
    PROJECT_TEMPLATE_UPDATED = "PROJECT_TEMPLATE_UPDATED"
    PROJECT_TEMPLATE_DELETED = "PROJECT_TEMPLATE_DELETED"


class Status26(Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class CreateWebHookDto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None
    url: str
    events: List[Event1]
    secretToken: Optional[constr(min_length=0, max_length=255)] = None
    hidden: Optional[bool] = Field(None, description="Default: false")
    status: Optional[Status26] = Field(None, description="Default: ENABLED")


class WebhookPreviewDto(BaseModel):
    event: Optional[str] = None
    preview: Optional[str] = None


class WebhookPreviewsDto(BaseModel):
    previews: Optional[List[WebhookPreviewDto]] = None


class PageDtoWebHookDtoV2(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[WebHookDtoV2]] = None


class ConceptDtov2(BaseModel):
    id: Optional[str] = None
    definition: Optional[str] = None
    domain: Optional[str] = None
    subDomains: Optional[List[str]] = None
    url: Optional[str] = None
    note: Optional[str] = None


class TermBaseReference(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None


class Status27(Enum):
    New = "New"
    Approved = "Approved"


class TermV2Dto(BaseModel):
    id: Optional[str] = None
    text: str
    lang: Optional[str] = None
    rtl: Optional[bool] = None
    modifiedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    modifiedBy: Optional[UserReference] = None
    createdBy: Optional[UserReference] = None
    caseSensitive: Optional[bool] = None
    exactMatch: Optional[bool] = None
    forbidden: Optional[bool] = None
    preferred: Optional[bool] = None
    status: Optional[Status27] = None
    conceptId: Optional[str] = None
    usage: Optional[str] = None
    note: Optional[str] = None
    writable: Optional[bool] = None
    shortTranslation: Optional[str] = None
    termType: Optional[str] = None
    partOfSpeech: Optional[str] = None
    gender: Optional[str] = None
    number: Optional[str] = None


class SearchTbByJobRequestDto(BaseModel):
    query: str
    count: Optional[int] = Field(None, description="Default: 15")
    offset: Optional[int] = Field(None, description="Default: 0")
    reverse: Optional[bool] = Field(None, description="Default: false")


class SearchInTextResponse2Dto(BaseModel):
    termBase: Optional[TermBaseReference] = None
    sourceTerm: Optional[TermV2Dto] = None
    concept: Optional[ConceptDtov2] = None
    translationTerms: Optional[List[TermV2Dto]] = None
    subTerm: Optional[bool] = None
    matches: Optional[List[Match]] = None


class SearchInTextResponseList2Dto(BaseModel):
    searchResults: Optional[List[SearchInTextResponse2Dto]] = None


class SearchTbInTextByJobRequestDto(BaseModel):
    text: str
    reverse: Optional[bool] = Field(None, description="Default: false")
    zeroLengthSeparator: Optional[str] = None


class Type15(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    PreAnalyseTarget = "PreAnalyseTarget"
    Compare = "Compare"
    PreAnalyseProvider = "PreAnalyseProvider"


class LoginResponseV3Dto(BaseModel):
    user: Optional[UserReference] = None
    token: Optional[str] = None
    expires: Optional[datetime] = None
    lastInvalidateAllSessionsPerformed: Optional[datetime] = None


class LoginV3Dto(BaseModel):
    userUid: Optional[str] = Field(
        None, description="When not filled, default user of identity will be logged in"
    )
    userName: str
    password: str
    code: Optional[str] = Field(
        None, description="Required only for 2-factor authentication"
    )


class LoginToSessionResponseV3Dto(BaseModel):
    user: Optional[UserReference] = None
    cookie: Optional[str] = None
    csrfToken: Optional[str] = None


class LoginToSessionV3Dto(BaseModel):
    userUid: Optional[str] = Field(
        None, description="When not filled, default user of identity will be logged in"
    )
    userName: str
    password: str
    rememberMe: Optional[bool] = None
    twoFactorCode: Optional[int] = None
    captchaCode: Optional[str] = None


class LoginOtherV3Dto(BaseModel):
    userUid: Optional[str] = Field(
        None, description="When not filled, default user of identity will be logged in"
    )
    userName: str


class ErrorDetailDtoV3(BaseModel):
    code: Optional[str] = Field(None, description="Code, e.g. NOT_FOUND.")
    args: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description='Related arguments, e.g. number => "hello world"'
    )
    message: Optional[str] = Field(None, description="Optional human-readable message.")


class JobPartPatchResultDto(BaseModel):
    updated: Optional[int] = Field(
        None, description="Number of successfully updated job parts"
    )
    errors: Optional[List[ErrorDetailDtoV3]] = Field(
        None, description="Errors and their counts encountered during the update"
    )


class Status28(Enum):
    NEW = "NEW"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"
    REJECTED = "REJECTED"
    DELIVERED = "DELIVERED"
    EMAILED = "EMAILED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class JobPartPatchBatchDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    status: Optional[Status28] = None
    dateDue: Optional[datetime] = None
    clearDateDue: Optional[bool] = None
    providers: Optional[List[ProviderReference]] = None


class SearchTMClientDtoV3(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class SearchTMDomainDtoV3(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class SearchTMProjectDtoV3(BaseModel):
    id: Optional[int] = None
    uid: Optional[str] = None
    name: Optional[str] = None


class SearchTMSubDomainDtoV3(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class SearchTMTransMemoryDtoV3(BaseModel):
    uid: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    reverse: Optional[bool] = None


class SearchTMByJobRequestDtoV3(BaseModel):
    query: str
    reverse: Optional[bool] = Field(None, description="Default: false")
    scoreThreshold: Optional[confloat(ge=0.0, le=1.01)] = Field(
        None, description="Default: 0.0"
    )
    maxResults: Optional[conint(ge=1, le=100)] = Field(None, description="Default: 15")


class WildCardSearchByJobRequestDtoV3(BaseModel):
    query: str
    reverse: Optional[bool] = Field(None, description="Default: false")
    count: Optional[conint(ge=1, le=50)] = None
    offset: Optional[int] = None


class MetadataOptionReference(BaseModel):
    uid: Optional[str] = None
    value: Optional[str] = None


class MetadataReference(BaseModel):
    uid: Optional[str] = None
    fieldName: Optional[str] = None
    value: Optional[str] = None
    options: Optional[List[MetadataOptionReference]] = None


class ProgressReference(BaseModel):
    totalCount: Optional[int] = None
    finishedCount: Optional[int] = None
    overdueCount: Optional[int] = None
    finishedRatio: Optional[float] = None
    overdueRatio: Optional[float] = None


class VendorUserReference(BaseModel):
    uid: Optional[str] = None
    vendorUid: Optional[str] = None
    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    organization: Optional[OrganizationReference] = None


class PreTranslateSettingsV3Dto(BaseModel):
    preTranslateOnJobCreation: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed: Pre-translate on job creation. Default: false",
    )
    setJobStatusCompleted: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed: Set job to completed once pre-translated. Default: false",
    )
    setJobStatusCompletedWhenConfirmed: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed when all segments confirmed:\nSet job to completed once pre-translated and all segments are confirmed. Default: false",
    )
    setProjectStatusCompleted: Optional[bool] = Field(
        None,
        description="Pre-translate & set job to completed: Set project to completed once all jobs pre-translated.\n        Default: false",
    )
    overwriteExistingTranslations: Optional[bool] = Field(
        None,
        description="Overwrite existing translations in target segments. Default: false",
    )
    translationMemorySettings: Optional[TranslationMemorySettingsDto] = None
    machineTranslationSettings: Optional[MachineTranslationSettingsDto] = None
    nonTranslatableSettings: Optional[NonTranslatableSettingsDto] = None
    repetitionsSettings: Optional[RepetitionsSettingsDto] = None


class CreateProjectV3Dto(BaseModel):
    name: constr(min_length=0, max_length=255)
    sourceLang: str
    targetLangs: List[str]
    client: Optional[IdReference] = Field(None, description="Client referenced by id")
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    costCenter: Optional[IdReference] = None
    purchaseOrder: Optional[constr(min_length=0, max_length=255)] = None
    workflowSteps: Optional[List[IdReference]] = None
    dateDue: Optional[datetime] = None
    note: Optional[constr(min_length=0, max_length=4096)] = None
    lqaProfiles: Optional[List[LqaProfilesForWsV2Dto]] = Field(
        None, description="Lqa profiles that will be added to workflow steps"
    )
    customFields: Optional[List[CustomFieldInstanceApiDto]] = Field(
        None, description="Custom fields for project"
    )
    fileHandover: Optional[bool] = Field(None, description="Default: false")


class AnalyseLanguagePartReference(BaseModel):
    id: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    jobs: Optional[List[AnalyseJobReference]] = None


class Type16(Enum):
    PreAnalyse = "PreAnalyse"
    PostAnalyse = "PostAnalyse"
    PreAnalyseTarget = "PreAnalyseTarget"
    Compare = "Compare"
    PreAnalyseProvider = "PreAnalyseProvider"


class AnalyseReference(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    innerId: Optional[str] = None
    type: Optional[Type16] = None
    name: Optional[str] = None
    provider: Optional[ProviderReference] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    netRateScheme: Optional[NetRateSchemeReference] = None
    analyseLanguageParts: Optional[List[AnalyseLanguagePartReference]] = None
    outdated: Optional[bool] = None
    importStatus: Optional[ImportStatusDto] = None
    pureWarnings: Optional[List[str]] = None


class PageDtoAnalyseReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[AnalyseReference]] = None


class MisspelledWordDto(BaseModel):
    word: Optional[str] = None
    offset: Optional[int] = None


class Position(BaseModel):
    beginIndex: Optional[int] = None
    endIndex: Optional[int] = None


class Term(BaseModel):
    text: Optional[str] = None
    preferred: Optional[bool] = None


class SegmentWarning(BaseModel):
    id: Optional[str] = None
    ignored: Optional[bool] = None
    type: Optional[str] = None
    repetitionGroupId: Optional[str] = None


class WarningType1(Enum):
    EmptyTranslation = "EmptyTranslation"
    TrailingPunctuation = "TrailingPunctuation"
    Formatting = "Formatting"
    JoinTags = "JoinTags"
    MissingNumbersV3 = "MissingNumbersV3"
    MultipleSpacesV3 = "MultipleSpacesV3"
    NonConformingTerm = "NonConformingTerm"
    NotConfirmed = "NotConfirmed"
    TranslationLength = "TranslationLength"
    AbsoluteLength = "AbsoluteLength"
    RelativeLength = "RelativeLength"
    UnresolvedComment = "UnresolvedComment"
    EmptyPairTags = "EmptyPairTags"
    InconsistentTranslationTargetSource = "InconsistentTranslationTargetSource"
    InconsistentTranslationSourceTarget = "InconsistentTranslationSourceTarget"
    ForbiddenString = "ForbiddenString"
    SpellCheck = "SpellCheck"
    RepeatedWord = "RepeatedWord"
    InconsistentTagContent = "InconsistentTagContent"
    EmptyTagContent = "EmptyTagContent"
    Malformed = "Malformed"
    ForbiddenTerm = "ForbiddenTerm"
    NewerAtLowerLevel = "NewerAtLowerLevel"
    LeadingAndTrailingSpaces = "LeadingAndTrailingSpaces"
    LeadingSpaces = "LeadingSpaces"
    TrailingSpaces = "TrailingSpaces"
    TargetSourceIdentical = "TargetSourceIdentical"
    SourceOrTargetRegexp = "SourceOrTargetRegexp"
    UnmodifiedFuzzyTranslation = "UnmodifiedFuzzyTranslation"
    UnmodifiedFuzzyTranslationTM = "UnmodifiedFuzzyTranslationTM"
    UnmodifiedFuzzyTranslationMTNT = "UnmodifiedFuzzyTranslationMTNT"
    Moravia = "Moravia"
    ExtraNumbersV3 = "ExtraNumbersV3"
    UnresolvedConversation = "UnresolvedConversation"
    NestedTags = "NestedTags"


class QualityAssuranceRunDtoV3(BaseModel):
    initialSegment: Optional[SegmentReference] = None
    maxQaWarningsCount: Optional[conint(ge=1, le=1000)] = Field(
        None,
        description="Maximum number of QA warnings in result, default: 100. For efficiency reasons QA\nwarnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned.",
    )
    warningTypes: Optional[List[WarningType1]] = Field(None, max_items=100, min_items=0)


class QualityAssuranceBatchRunDtoV3(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=500, min_items=1)
    settings: Optional[QualityAssuranceRunDtoV3] = None
    maxQaWarningsCount: Optional[conint(ge=1, le=1000)] = Field(
        None,
        description="Maximum number of QA warnings in result, default: 100. For efficiency reasons QA\nwarnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned.",
    )


class JobPartSegmentsDtoV3(BaseModel):
    job: UidReference
    segments: List[str]


class WarningType2(Enum):
    EmptyTranslation = "EmptyTranslation"
    TrailingPunctuation = "TrailingPunctuation"
    Formatting = "Formatting"
    JoinTags = "JoinTags"
    MissingNumbersV3 = "MissingNumbersV3"
    MultipleSpacesV3 = "MultipleSpacesV3"
    NonConformingTerm = "NonConformingTerm"
    NotConfirmed = "NotConfirmed"
    TranslationLength = "TranslationLength"
    AbsoluteLength = "AbsoluteLength"
    RelativeLength = "RelativeLength"
    UnresolvedComment = "UnresolvedComment"
    EmptyPairTags = "EmptyPairTags"
    InconsistentTranslationTargetSource = "InconsistentTranslationTargetSource"
    InconsistentTranslationSourceTarget = "InconsistentTranslationSourceTarget"
    ForbiddenString = "ForbiddenString"
    SpellCheck = "SpellCheck"
    RepeatedWord = "RepeatedWord"
    InconsistentTagContent = "InconsistentTagContent"
    EmptyTagContent = "EmptyTagContent"
    Malformed = "Malformed"
    ForbiddenTerm = "ForbiddenTerm"
    NewerAtLowerLevel = "NewerAtLowerLevel"
    LeadingAndTrailingSpaces = "LeadingAndTrailingSpaces"
    LeadingSpaces = "LeadingSpaces"
    TrailingSpaces = "TrailingSpaces"
    TargetSourceIdentical = "TargetSourceIdentical"
    SourceOrTargetRegexp = "SourceOrTargetRegexp"
    UnmodifiedFuzzyTranslation = "UnmodifiedFuzzyTranslation"
    UnmodifiedFuzzyTranslationTM = "UnmodifiedFuzzyTranslationTM"
    UnmodifiedFuzzyTranslationMTNT = "UnmodifiedFuzzyTranslationMTNT"
    Moravia = "Moravia"
    ExtraNumbersV3 = "ExtraNumbersV3"
    UnresolvedConversation = "UnresolvedConversation"
    NestedTags = "NestedTags"


class QualityAssuranceSegmentsRunDtoV3(BaseModel):
    jobsAndSegments: List[JobPartSegmentsDtoV3] = Field(..., max_items=100, min_items=1)
    warningTypes: Optional[List[WarningType2]] = Field(
        None, description="When empty only fast checks run", max_items=100, min_items=0
    )
    maxQaWarningsCount: Optional[conint(ge=1, le=1000)] = Field(
        None,
        description="Maximum number of QA warnings in result, default: 100. For efficiency reasons QA\nwarnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned.",
    )


class JobExportResponseDto(BaseModel):
    jobs: Optional[List[UidReference]] = None


class JobExportActionDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=1000, min_items=1)


class TransMemoryDtoV3(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    internalId: Optional[int] = None
    name: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    client: Optional[ClientReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    note: Optional[str] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None


class WorkflowStepReferenceV3(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    uid: Optional[str] = None
    order: Optional[int] = None
    lqaEnabled: Optional[bool] = None


class ProjectTransMemoryDtoV3(BaseModel):
    transMemory: Optional[TransMemoryDtoV3] = None
    penalty: Optional[float] = None
    applyPenaltyTo101Only: Optional[bool] = None
    targetLocale: Optional[str] = None
    workflowStep: Optional[WorkflowStepReferenceV3] = None
    readMode: Optional[bool] = None
    writeMode: Optional[bool] = None
    order: Optional[int] = None


class ProjectTransMemoryListDtoV3(BaseModel):
    transMemories: Optional[List[ProjectTransMemoryDtoV3]] = None


class SetProjectTransMemoryV3Dto(BaseModel):
    transMemory: UidReference
    readMode: Optional[bool] = Field(None, description="Default: false")
    writeMode: Optional[bool] = Field(
        None,
        description="Can be set only for Translation Memory with read == true.<br/>\n        Max 2 write TMs allowed per project.<br/>\n        Default: false",
    )
    penalty: Optional[confloat(ge=0.0, le=100.0)] = None
    applyPenaltyTo101Only: Optional[bool] = Field(
        None, description="Can be set only for penalty == 1<br/>Default: false"
    )
    order: Optional[int] = None


class Role4(Enum):
    SYS_ADMIN = "SYS_ADMIN"
    SYS_ADMIN_READ = "SYS_ADMIN_READ"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LINGUIST = "LINGUIST"
    GUEST = "GUEST"
    SUBMITTER = "SUBMITTER"


class UserDetailsDtoV3(BaseModel):
    uid: constr(min_length=0, max_length=255)
    userName: constr(min_length=0, max_length=255)
    firstName: constr(min_length=0, max_length=255)
    lastName: constr(min_length=0, max_length=255)
    email: constr(min_length=0, max_length=255)
    dateCreated: Optional[datetime] = None
    dateDeleted: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    role: Role4 = Field(
        ...,
        description='Enum: "ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER"',
    )
    timezone: constr(min_length=0, max_length=255)
    note: Optional[constr(min_length=0, max_length=4096)] = None
    receiveNewsletter: Optional[bool] = None
    active: Optional[bool] = None


class Role5(Enum):
    SYS_ADMIN = "SYS_ADMIN"
    SYS_ADMIN_READ = "SYS_ADMIN_READ"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LINGUIST = "LINGUIST"
    GUEST = "GUEST"
    SUBMITTER = "SUBMITTER"


class AbstractUserEditDto(BaseModel):
    userName: constr(min_length=0, max_length=255)
    firstName: constr(min_length=0, max_length=255)
    lastName: constr(min_length=0, max_length=255)
    email: constr(min_length=0, max_length=255)
    role: Role5 = Field(
        ...,
        description='Enum: "ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER"',
    )
    timezone: constr(min_length=0, max_length=255)
    receiveNewsletter: Optional[bool] = Field(None, description="Default: true")
    note: Optional[constr(min_length=0, max_length=4096)] = None
    active: Optional[bool] = Field(None, description="Default: true")


class GUESTEDIT(AbstractUserEditDto):
    client: UidReference
    enableMT: Optional[bool] = Field(None, description="Enable MT. Default: true")
    projectViewOther: Optional[bool] = Field(
        None, description="View projects created by other users. Default: true"
    )
    projectViewOtherLinguist: Optional[bool] = Field(
        None, description="Show provider names. Default: true"
    )
    projectViewOtherEditor: Optional[bool] = Field(
        None, description="Edit jobs in Memsource Editor. Default: true"
    )
    transMemoryViewOther: Optional[bool] = Field(
        None, description="View TMs created by other users. Default: true"
    )
    transMemoryEditOther: Optional[bool] = Field(
        None, description="Modify TMs created by other users. Default: true"
    )
    transMemoryExportOther: Optional[bool] = Field(
        None, description="Export TMs created by other users. Default: true"
    )
    transMemoryImportOther: Optional[bool] = Field(
        None, description="Import into TMs created by other users. Default: true"
    )
    termBaseViewOther: Optional[bool] = Field(
        None, description="View TBs created by other users. Default: true"
    )
    termBaseEditOther: Optional[bool] = Field(
        None, description="Modify TBs created by other users. Default: true"
    )
    termBaseExportOther: Optional[bool] = Field(
        None, description="Export TBs created by other users. Default: true"
    )
    termBaseImportOther: Optional[bool] = Field(
        None, description="Import into TBs created by other users. Default: true"
    )
    termBaseApproveOther: Optional[bool] = Field(
        None, description="Approve terms in TBs created by other users. Default: true"
    )


class LINGUISTEDIT(AbstractUserEditDto):
    editAllTermsInTB: Optional[bool] = Field(
        None, description="Edit all terms in TB. Default: false"
    )
    editTranslationsInTM: Optional[bool] = Field(
        None, description="Edit translations in TM. Default: false"
    )
    enableMT: Optional[bool] = Field(None, description="Enable MT. Default: true")
    mayRejectJobs: Optional[bool] = Field(
        None, description="Reject jobs. Default: false"
    )
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    workflowSteps: Optional[List[UidReference]] = None
    clients: Optional[List[UidReference]] = None
    domains: Optional[List[UidReference]] = None
    subDomains: Optional[List[UidReference]] = None
    netRateScheme: Optional[UidReference] = Field(None, description="Net rate scheme")
    translationPriceList: Optional[UidReference] = Field(None, description="Price list")


class DashboardSetting(Enum):
    ALL_DATA = "ALL_DATA"
    OWN_DATA = "OWN_DATA"
    NO_DASHBOARD = "NO_DASHBOARD"


class PROJECTMANAGEREDIT(AbstractUserEditDto):
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    workflowSteps: Optional[List[UidReference]] = None
    clients: Optional[List[UidReference]] = None
    domains: Optional[List[UidReference]] = None
    subDomains: Optional[List[UidReference]] = None
    projectCreate: Optional[bool] = Field(
        None, description="Enable project creation. Default: true"
    )
    projectViewOther: Optional[bool] = Field(
        None, description="View projects created by other users. Default: true"
    )
    projectEditOther: Optional[bool] = Field(
        None, description="Modify projects created by other users. Default: true"
    )
    projectDeleteOther: Optional[bool] = Field(
        None, description="Delete projects created by other users. Default: true"
    )
    projectClients: Optional[List[UidReference]] = Field(
        None, description="Access projects of a selected clients only"
    )
    projectBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access projects of selected business units only"
    )
    projectTemplateCreate: Optional[bool] = Field(
        None, description="Enable project templates creation. Default: true"
    )
    projectTemplateViewOther: Optional[bool] = Field(
        None, description="View project templates created by other users. Default: true"
    )
    projectTemplateEditOther: Optional[bool] = Field(
        None,
        description="Modify project templates created by other users. Default: true",
    )
    projectTemplateDeleteOther: Optional[bool] = Field(
        None,
        description="Delete project templates created by other users. Default: true",
    )
    projectTemplateClients: Optional[List[UidReference]] = Field(
        None, description="Access project templates of a selected clients only"
    )
    projectTemplateBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access project templates of selected business units only"
    )
    transMemoryCreate: Optional[bool] = Field(
        None, description="Enable TMs creation. Default: true"
    )
    transMemoryViewOther: Optional[bool] = Field(
        None, description="View TMs created by other users. Default: true"
    )
    transMemoryEditOther: Optional[bool] = Field(
        None, description="Modify TMs created by other users. Default: true"
    )
    transMemoryDeleteOther: Optional[bool] = Field(
        None, description="Delete TMs created by other users. Default: true"
    )
    transMemoryExportOther: Optional[bool] = Field(
        None, description="Export TMs created by other users. Default: true"
    )
    transMemoryImportOther: Optional[bool] = Field(
        None, description="Import into TMs created by other users. Default: true"
    )
    transMemoryClients: Optional[List[UidReference]] = Field(
        None, description="Access TMs of a selected clients only"
    )
    transMemoryBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access TMs of selected business units only"
    )
    termBaseCreate: Optional[bool] = Field(
        None, description="Enable TBs creation. Default: true"
    )
    termBaseViewOther: Optional[bool] = Field(
        None, description="View TBs created by other users. Default: true"
    )
    termBaseEditOther: Optional[bool] = Field(
        None, description="Modify TBs created by other users. Default: true"
    )
    termBaseDeleteOther: Optional[bool] = Field(
        None, description="Delete TBs created by other users. Default: true"
    )
    termBaseExportOther: Optional[bool] = Field(
        None, description="Export TBs created by other users. Default: true"
    )
    termBaseImportOther: Optional[bool] = Field(
        None, description="Import into TBs created by other users. Default: true"
    )
    termBaseApproveOther: Optional[bool] = Field(
        None, description="Approve terms in TBs created by other users. Default: true"
    )
    termBaseClients: Optional[List[UidReference]] = Field(
        None, description="Access TBs of a selected clients only"
    )
    termBaseBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access TBs of selected business units only"
    )
    userCreate: Optional[bool] = Field(
        None, description="Enable users creation. Default: true"
    )
    userViewOther: Optional[bool] = Field(
        None, description="View users created by other users. Default: true"
    )
    userEditOther: Optional[bool] = Field(
        None, description="Modify users created by other users. Default: true"
    )
    userDeleteOther: Optional[bool] = Field(
        None, description="Delete users created by other users. Default: true"
    )
    clientDomainSubDomainCreate: Optional[bool] = Field(
        None, description="Enable clients, domains, subdomains creation. Default: true"
    )
    clientDomainSubDomainViewOther: Optional[bool] = Field(
        None,
        description="View clients, domains, subdomains created by other users. Default: true",
    )
    clientDomainSubDomainEditOther: Optional[bool] = Field(
        None,
        description="Modify clients, domains, subdomains created by other users. Default: true",
    )
    clientDomainSubDomainDeleteOther: Optional[bool] = Field(
        None,
        description="Delete clients, domains, subdomains created by other users. Default: true",
    )
    vendorCreate: Optional[bool] = Field(
        None, description="Enable Vendors creation. Default: true"
    )
    vendorViewOther: Optional[bool] = Field(
        None, description="View Vendors created by other users. Default: true"
    )
    vendorEditOther: Optional[bool] = Field(
        None, description="Modify Vendors created by other users. Default: true"
    )
    vendorDeleteOther: Optional[bool] = Field(
        None, description="Delete Vendors created by other users. Default: true"
    )
    dashboardSetting: Optional[DashboardSetting] = Field(
        None, description="Home page dashboards. Default: OWN_DATA"
    )
    setupServer: Optional[bool] = Field(
        None, description="Modify setup's server settings. Default: true"
    )


class SUBMITTEREDIT(AbstractUserEditDto):
    automationWidgets: List[IdReference]
    projectViewCreatedByOtherSubmitters: Optional[bool] = Field(
        None, description="View projects created by other Submitters. Default: false"
    )


class Role6(Enum):
    SYS_ADMIN = "SYS_ADMIN"
    SYS_ADMIN_READ = "SYS_ADMIN_READ"
    ADMIN = "ADMIN"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LINGUIST = "LINGUIST"
    GUEST = "GUEST"
    SUBMITTER = "SUBMITTER"


class AbstractUserCreateDto(BaseModel):
    userName: constr(min_length=0, max_length=255)
    firstName: constr(min_length=0, max_length=255)
    lastName: constr(min_length=0, max_length=255)
    email: constr(min_length=0, max_length=255)
    password: constr(min_length=0, max_length=255)
    role: Role6 = Field(
        ...,
        description='Enum: "ADMIN", "PROJECT_MANAGER", "LINGUIST", "GUEST", "SUBMITTER"',
    )
    timezone: constr(min_length=0, max_length=255)
    receiveNewsletter: Optional[bool] = Field(None, description="Default: true")
    note: Optional[constr(min_length=0, max_length=4096)] = None
    active: Optional[bool] = Field(None, description="Default: true")


class GUEST(AbstractUserCreateDto):
    client: UidReference
    enableMT: Optional[bool] = Field(None, description="Enable MT. Default: true")
    projectViewOther: Optional[bool] = Field(
        None, description="View projects created by other users. Default: true"
    )
    projectViewOtherLinguist: Optional[bool] = Field(
        None, description="Show provider names. Default: true"
    )
    projectViewOtherEditor: Optional[bool] = Field(
        None, description="Edit jobs in Memsource Editor. Default: true"
    )
    transMemoryViewOther: Optional[bool] = Field(
        None, description="View TMs created by other users. Default: true"
    )
    transMemoryEditOther: Optional[bool] = Field(
        None, description="Modify TMs created by other users. Default: true"
    )
    transMemoryExportOther: Optional[bool] = Field(
        None, description="Export TMs created by other users. Default: true"
    )
    transMemoryImportOther: Optional[bool] = Field(
        None, description="Import into TMs created by other users. Default: true"
    )
    termBaseViewOther: Optional[bool] = Field(
        None, description="View TBs created by other users. Default: true"
    )
    termBaseEditOther: Optional[bool] = Field(
        None, description="Modify TBs created by other users. Default: true"
    )
    termBaseExportOther: Optional[bool] = Field(
        None, description="Export TBs created by other users. Default: true"
    )
    termBaseImportOther: Optional[bool] = Field(
        None, description="Import into TBs created by other users. Default: true"
    )
    termBaseApproveOther: Optional[bool] = Field(
        None, description="Approve terms in TBs created by other users. Default: true"
    )


class LINGUIST(AbstractUserCreateDto):
    editAllTermsInTB: Optional[bool] = Field(
        None, description="Edit all terms in TB. Default: false"
    )
    editTranslationsInTM: Optional[bool] = Field(
        None, description="Edit translations in TM. Default: false"
    )
    enableMT: Optional[bool] = Field(None, description="Enable MT. Default: true")
    mayRejectJobs: Optional[bool] = Field(
        None, description="Reject jobs. Default: false"
    )
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    workflowSteps: Optional[List[UidReference]] = None
    clients: Optional[List[UidReference]] = None
    domains: Optional[List[UidReference]] = None
    subDomains: Optional[List[UidReference]] = None
    netRateScheme: Optional[UidReference] = Field(None, description="Net rate scheme")
    translationPriceList: Optional[UidReference] = Field(None, description="Price list")


class DashboardSetting1(Enum):
    ALL_DATA = "ALL_DATA"
    OWN_DATA = "OWN_DATA"
    NO_DASHBOARD = "NO_DASHBOARD"


class PROJECTMANAGER(AbstractUserCreateDto):
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    workflowSteps: Optional[List[UidReference]] = None
    clients: Optional[List[UidReference]] = None
    domains: Optional[List[UidReference]] = None
    subDomains: Optional[List[UidReference]] = None
    projectCreate: Optional[bool] = Field(
        None, description="Enable project creation. Default: true"
    )
    projectViewOther: Optional[bool] = Field(
        None, description="View projects created by other users. Default: true"
    )
    projectEditOther: Optional[bool] = Field(
        None, description="Modify projects created by other users. Default: true"
    )
    projectDeleteOther: Optional[bool] = Field(
        None, description="Delete projects created by other users. Default: true"
    )
    projectClients: Optional[List[UidReference]] = Field(
        None, description="Access projects of a selected clients only"
    )
    projectBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access projects of selected business units only"
    )
    projectTemplateCreate: Optional[bool] = Field(
        None, description="Enable project templates creation. Default: true"
    )
    projectTemplateViewOther: Optional[bool] = Field(
        None, description="View project templates created by other users. Default: true"
    )
    projectTemplateEditOther: Optional[bool] = Field(
        None,
        description="Modify project templates created by other users. Default: true",
    )
    projectTemplateDeleteOther: Optional[bool] = Field(
        None,
        description="Delete project templates created by other users. Default: true",
    )
    projectTemplateClients: Optional[List[UidReference]] = Field(
        None, description="Access project templates of a selected clients only"
    )
    projectTemplateBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access project templates of selected business units only"
    )
    transMemoryCreate: Optional[bool] = Field(
        None, description="Enable TMs creation. Default: true"
    )
    transMemoryViewOther: Optional[bool] = Field(
        None, description="View TMs created by other users. Default: true"
    )
    transMemoryEditOther: Optional[bool] = Field(
        None, description="Modify TMs created by other users. Default: true"
    )
    transMemoryDeleteOther: Optional[bool] = Field(
        None, description="Delete TMs created by other users. Default: true"
    )
    transMemoryExportOther: Optional[bool] = Field(
        None, description="Export TMs created by other users. Default: true"
    )
    transMemoryImportOther: Optional[bool] = Field(
        None, description="Import into TMs created by other users. Default: true"
    )
    transMemoryClients: Optional[List[UidReference]] = Field(
        None, description="Access TMs of a selected clients only"
    )
    transMemoryBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access TMs of selected business units only"
    )
    termBaseCreate: Optional[bool] = Field(
        None, description="Enable TBs creation. Default: true"
    )
    termBaseViewOther: Optional[bool] = Field(
        None, description="View TBs created by other users. Default: true"
    )
    termBaseEditOther: Optional[bool] = Field(
        None, description="Modify TBs created by other users. Default: true"
    )
    termBaseDeleteOther: Optional[bool] = Field(
        None, description="Delete TBs created by other users. Default: true"
    )
    termBaseExportOther: Optional[bool] = Field(
        None, description="Export TBs created by other users. Default: true"
    )
    termBaseImportOther: Optional[bool] = Field(
        None, description="Import into TBs created by other users. Default: true"
    )
    termBaseApproveOther: Optional[bool] = Field(
        None, description="Approve terms in TBs created by other users. Default: true"
    )
    termBaseClients: Optional[List[UidReference]] = Field(
        None, description="Access TBs of a selected clients only"
    )
    termBaseBusinessUnits: Optional[List[UidReference]] = Field(
        None, description="Access TBs of selected business units only"
    )
    userCreate: Optional[bool] = Field(
        None, description="Enable users creation. Default: true"
    )
    userViewOther: Optional[bool] = Field(
        None, description="View users created by other users. Default: true"
    )
    userEditOther: Optional[bool] = Field(
        None, description="Modify users created by other users. Default: true"
    )
    userDeleteOther: Optional[bool] = Field(
        None, description="Delete users created by other users. Default: true"
    )
    clientDomainSubDomainCreate: Optional[bool] = Field(
        None, description="Enable clients, domains, subdomains creation. Default: true"
    )
    clientDomainSubDomainViewOther: Optional[bool] = Field(
        None,
        description="View clients, domains, subdomains created by other users. Default: true",
    )
    clientDomainSubDomainEditOther: Optional[bool] = Field(
        None,
        description="Modify clients, domains, subdomains created by other users. Default: true",
    )
    clientDomainSubDomainDeleteOther: Optional[bool] = Field(
        None,
        description="Delete clients, domains, subdomains created by other users. Default: true",
    )
    vendorCreate: Optional[bool] = Field(
        None, description="Enable Vendors creation. Default: true"
    )
    vendorViewOther: Optional[bool] = Field(
        None, description="View Vendors created by other users. Default: true"
    )
    vendorEditOther: Optional[bool] = Field(
        None, description="Modify Vendors created by other users. Default: true"
    )
    vendorDeleteOther: Optional[bool] = Field(
        None, description="Delete Vendors created by other users. Default: true"
    )
    dashboardSetting: Optional[DashboardSetting1] = Field(
        None, description="Home page dashboards. Default: OWN_DATA"
    )
    setupServer: Optional[bool] = Field(
        None, description="Modify setup's server settings. Default: true"
    )


class SUBMITTER(AbstractUserCreateDto):
    automationWidgets: Optional[List[IdReference]] = Field(
        None,
        description="If no automation widgets are assigned in request the default automation widgets will be assigned instead",
    )
    projectViewCreatedByOtherSubmitters: Optional[bool] = Field(
        None, description="View projects created by other Submitters. Default: false"
    )


class AsyncResponseDto(BaseModel):
    dateCreated: Optional[datetime] = None
    errorCode: Optional[str] = None
    errorDesc: Optional[str] = None
    errorDetails: Optional[List[ErrorDetailDto]] = None
    warnings: Optional[List[ErrorDetailDto]] = None
    acceptedSegmentsCount: Optional[int] = None


class ProjectReference(BaseModel):
    uid: Optional[str] = None
    innerId: Optional[int] = None
    name: Optional[str] = None
    businessUnit: Optional[BusinessUnitReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    client: Optional[ClientReference] = None
    costCenter: Optional[CostCenterReference] = None
    dueDate: Optional[datetime] = None
    createdDate: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    owner: Optional[UserReference] = None
    vendor: Optional[VendorUserReference] = None
    purchaseOrder: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    status: Optional[str] = None
    progress: Optional[ProgressReference] = None
    metadata: Optional[List[MetadataReference]] = None
    note: Optional[str] = None
    deleted: Optional[bool] = None
    archived: Optional[bool] = None


class DataDtoV1(BaseModel):
    available: Optional[bool] = None
    all: Optional[CountsDto] = None
    repetitions: Optional[CountsDto] = None
    transMemoryMatches: Optional[MatchCounts101Dto] = None
    machineTranslationMatches: Optional[MatchCountsDto] = None
    nonTranslatablesMatches: Optional[MatchCountsNTDtoV1] = None
    internalFuzzyMatches: Optional[MatchCountsDto] = None


class AnalyseJobDto(BaseModel):
    uid: Optional[str] = None
    filename: Optional[str] = None
    data: Optional[DataDtoV1] = None
    discountedData: Optional[DataDtoV1] = None


class PageDtoAnalyseJobDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[AnalyseJobDto]] = None


class AsyncRequestStatusDto(BaseModel):
    concurrentRequests: Optional[ConcurrentRequestsDto] = Field(
        None, description="Current count of running requests and the allowed limit"
    )


class LoginUserDto(BaseModel):
    user: Optional[UserReference] = None
    csrfToken: Optional[str] = None
    organization: Optional[OrganizationReference] = None
    edition: Optional[EditionDto] = None
    features: Optional[FeaturesDto] = None


class JobPartReference(BaseModel):
    uid: Optional[str] = None
    status: Optional[Status] = None
    providers: Optional[List[ProviderReference]] = None
    targetLang: Optional[str] = None
    workflowLevel: Optional[int] = None
    workflowStep: Optional[WorkflowStepReference] = None
    filename: Optional[str] = None
    dateDue: Optional[datetime] = None
    dateCreated: Optional[datetime] = None
    updateSourceDate: Optional[datetime] = None
    imported: Optional[bool] = None
    jobAssignedEmailTemplate: Optional[ObjectReference] = None
    notificationIntervalInMinutes: Optional[int] = None
    continuous: Optional[bool] = None
    sourceFileUid: Optional[str] = None


class JobPartsDto(BaseModel):
    jobs: Optional[List[JobPartReference]] = None


class ClientDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    externalId: Optional[str] = None
    note: Optional[str] = None
    displayNoteInProject: Optional[bool] = Field(None, description="Default: false")
    priceList: Optional[PriceListReference] = None
    netRateScheme: Optional[NetRateSchemeReference] = None
    createdBy: Optional[UserReference] = None


class PageDtoClientDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[ClientDto]] = None


class AutomatedProjectSettingsDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    organization: Optional[NameDto] = None
    active: Optional[bool] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = Field(None, unique_items=True)
    connector: Optional[NameDto] = None
    remoteFolder: Optional[str] = None


class ConnectorDto(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[Type1] = None
    organization: Optional[NameDto] = None
    createdBy: Optional[NameDto] = None
    createdAt: Optional[datetime] = None
    localToken: Optional[str] = None
    automatedProjectSettings: Optional[List[AutomatedProjectSettingsDto]] = None


class Marketo(AbstractConnectorDto):
    apiKey: str
    apiSecret: str
    identityURL: str
    connectorType: str
    variables: Optional[List[VariableDto]] = None
    segmentationMapping: Optional[MarketoSegmentationMappingDto] = None
    translateTokens: Optional[bool] = None
    debugMode: Optional[bool] = None


class ConnectorListDto(BaseModel):
    connectors: Optional[List[ConnectorDto]] = None
    totalCount: Optional[int] = None


class LQAReferences(BaseModel):
    taskId: Optional[str] = None
    jobPartUid: Optional[str] = None
    transGroupId: conint(ge=0)
    segmentId: str
    conversationTitle: Optional[str] = None
    conversationTitleOffset: Optional[conint(ge=0)] = None
    commentedText: Optional[str] = None
    correlation: Optional[ReferenceCorrelation] = None
    lqa: List[LQAReference] = Field(..., max_items=2147483647, min_items=1)


class PlainReferences(BaseModel):
    taskId: Optional[str] = None
    jobPartUid: Optional[str] = None
    transGroupId: conint(ge=0)
    segmentId: str
    conversationTitle: Optional[str] = None
    conversationTitleOffset: Optional[conint(ge=0)] = None
    commentedText: Optional[str] = None
    correlation: Optional[ReferenceCorrelation] = None


class ProjectWorkflowStepDtoV2(BaseModel):
    id: Optional[int] = None
    abbreviation: Optional[str] = None
    name: Optional[str] = None
    workflowLevel: Optional[int] = None
    workflowStep: Optional[WorkflowStepReferenceV2] = None


class FileImportSettingsDto(BaseModel):
    inputCharset: Optional[str] = None
    outputCharset: Optional[str] = None
    zipCharset: Optional[str] = None
    fileFormat: Optional[str] = None
    autodetectMultilingualFiles: Optional[bool] = None
    targetLength: Optional[bool] = None
    targetLengthMax: Optional[int] = None
    targetLengthPercent: Optional[bool] = None
    targetLengthPercentValue: Optional[float] = None
    android: Optional[AndroidSettingsDto] = None
    idml: Optional[IdmlSettingsDto] = None
    xls: Optional[XlsSettingsDto] = None
    multilingualXml: Optional[MultilingualXmlSettingsDto] = None
    php: Optional[PhpSettingsDto] = None
    resx: Optional[ResxSettingsDto] = None
    json_: Optional[JsonSettingsDto] = Field(None, alias="json")
    html: Optional[HtmlSettingsDto] = None
    multilingualXls: Optional[MultilingualXlsSettingsDto] = None
    multilingualCsv: Optional[MultilingualCsvSettingsDto] = None
    csv: Optional[CsvSettingsDto] = None
    txt: Optional[TxtSettingsDto] = None
    xlf2: Optional[Xlf2SettingsDto] = None
    quarkTag: Optional[QuarkTagSettingsDto] = None
    pdf: Optional[PdfSettingsDto] = None
    tmMatch: Optional[TMMatchSettingsDto] = None
    xml: Optional[XmlSettingsDto] = None
    mif: Optional[MifSettingsDto] = None
    properties: Optional[PropertiesSettingsDto] = None
    doc: Optional[DocSettingsDto] = None
    xlf: Optional[XlfSettingsDto] = None
    sdlXlf: Optional[SdlXlfSettingsDto] = None
    ttx: Optional[TtxSettingsDto] = None
    ppt: Optional[PptSettingsDto] = None
    yaml: Optional[YamlSettingsDto] = None
    dita: Optional[DitaSettingsDto] = None
    docBook: Optional[DocBookSettingsDto] = None
    po: Optional[PoSettingsDto] = None
    mac: Optional[MacSettingsDto] = None
    md: Optional[MdSettingsDto] = None
    psd: Optional[PsdSettingsDto] = None
    asciidoc: Optional[AsciidocSettingsDto] = None
    segRule: Optional[SegRuleReference] = None
    targetSegRule: Optional[SegRuleReference] = None


class CreateCustomFileTypeDto(BaseModel):
    name: str
    filenamePattern: str
    type: Type4
    fileImportSettings: Optional[FileImportSettingsCreateDto] = None


class NetRateScheme(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    name: Optional[str] = None
    organization: Optional[OrganizationReference] = None
    dateCreated: Optional[datetime] = None
    createdBy: Optional[UserReference] = None
    workflowStepNetSchemes: Optional[List[NetRateSchemeWorkflowStepReference]] = None
    rates: Optional[DiscountSettingsDto] = None


class DiscountSchemeCreateDto(BaseModel):
    name: constr(min_length=1, max_length=255)
    rates: Optional[DiscountSettingsDto] = None
    workflowStepNetSchemes: Optional[List[NetRateSchemeWorkflowStepCreate]] = None


class GlossaryDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    internalId: Optional[int] = None
    name: str
    langs: Optional[List[str]] = None
    createdBy: Optional[UserReference] = None
    owner: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    profileCount: Optional[int] = None
    active: Optional[bool] = None
    profiles: Optional[List[MemsourceTranslateProfileSimpleDto]] = None


class PageDtoGlossaryDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[GlossaryDto]] = None


class SearchTMSegmentDto(BaseModel):
    id: Optional[str] = None
    text: Optional[str] = None
    lang: Optional[str] = None
    rtl: Optional[bool] = None
    modifiedAt: Optional[int] = None
    createdAt: Optional[int] = None
    modifiedBy: Optional[UserReference] = None
    createdBy: Optional[UserReference] = None
    filename: Optional[str] = None
    project: Optional[SearchTMProjectDto] = None
    client: Optional[SearchTMClientDto] = None
    domain: Optional[SearchTMDomainDto] = None
    subDomain: Optional[SearchTMSubDomainDto] = None
    tagMetadata: Optional[List[TagMetadata]] = None
    previousSegment: Optional[str] = None
    nextSegment: Optional[str] = None
    key: Optional[str] = None


class SearchTMByJobRequestDto(BaseModel):
    segment: str
    workflowLevel: Optional[conint(ge=1, le=15)] = None
    scoreThreshold: Optional[confloat(ge=0.0, le=1.01)] = None
    previousSegment: Optional[str] = None
    nextSegment: Optional[str] = None
    contextKey: Optional[str] = None
    maxSegments: Optional[conint(ge=0, le=5)] = Field(None, description="Default: 5")
    maxSubSegments: Optional[conint(ge=0, le=5)] = Field(None, description="Default: 5")
    tagMetadata: Optional[List[TagMetadataDto]] = None


class AccuracyWeightsDto(BaseModel):
    accuracy: Optional[ToggleableWeightDto] = None
    addition: Optional[ToggleableWeightDto] = None
    omission: Optional[ToggleableWeightDto] = None
    mistranslation: Optional[ToggleableWeightDto] = None
    underTranslation: Optional[ToggleableWeightDto] = None
    untranslated: Optional[ToggleableWeightDto] = None
    improperTmMatch: Optional[ToggleableWeightDto] = None
    overTranslation: Optional[ToggleableWeightDto] = None


class DesignWeightsDto(BaseModel):
    design: Optional[ToggleableWeightDto] = None
    length: Optional[ToggleableWeightDto] = None
    localFormatting: Optional[ToggleableWeightDto] = None
    markup: Optional[ToggleableWeightDto] = None
    missingText: Optional[ToggleableWeightDto] = None
    truncation: Optional[ToggleableWeightDto] = None


class FluencyWeightsDto(BaseModel):
    fluency: Optional[ToggleableWeightDto] = None
    punctuation: Optional[ToggleableWeightDto] = None
    spelling: Optional[ToggleableWeightDto] = None
    grammar: Optional[ToggleableWeightDto] = None
    grammaticalRegister: Optional[ToggleableWeightDto] = None
    inconsistency: Optional[ToggleableWeightDto] = None
    crossReference: Optional[ToggleableWeightDto] = None
    characterEncoding: Optional[ToggleableWeightDto] = None


class LocaleConventionWeightsDto(BaseModel):
    localeConvention: Optional[ToggleableWeightDto] = None
    addressFormat: Optional[ToggleableWeightDto] = None
    dateFormat: Optional[ToggleableWeightDto] = None
    currencyFormat: Optional[ToggleableWeightDto] = None
    measurementFormat: Optional[ToggleableWeightDto] = None
    shortcutKey: Optional[ToggleableWeightDto] = None
    telephoneFormat: Optional[ToggleableWeightDto] = None


class OtherWeightsDto(BaseModel):
    other: Optional[ToggleableWeightDto] = None


class PenaltyPointsDto(BaseModel):
    neutral: Optional[SeverityDto] = None
    minor: Optional[SeverityDto] = None
    major: Optional[SeverityDto] = None
    critical: Optional[SeverityDto] = None


class StyleWeightsDto(BaseModel):
    style: Optional[ToggleableWeightDto] = None
    awkward: Optional[ToggleableWeightDto] = None
    companyStyle: Optional[ToggleableWeightDto] = None
    inconsistentStyle: Optional[ToggleableWeightDto] = None
    thirdPartyStyle: Optional[ToggleableWeightDto] = None
    unidiomatic: Optional[ToggleableWeightDto] = None


class TerminologyWeightsDto(BaseModel):
    terminology: Optional[ToggleableWeightDto] = None
    inconsistentWithTb: Optional[ToggleableWeightDto] = None
    inconsistentUseOfTerminology: Optional[ToggleableWeightDto] = None


class ImportSettingsDto(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    fileImportSettings: Optional[FileImportSettingsDto] = None


class MORAVIA(QACheckDtoV2):
    enabled: Optional[bool] = None
    profile: Optional[str] = None
    ignorable: Optional[bool] = None
    instant: Optional[bool] = None


class NUMBER(QACheckDtoV2):
    ignorable: Optional[bool] = None
    enabled: Optional[bool] = None
    value: Optional[Number] = None
    instant: Optional[bool] = None


class REGEX(QACheckDtoV2):
    rules: Optional[List[RegexpCheckRuleDtoV2]] = None


class AbstractProjectDto(BaseModel):
    uid: Optional[str] = None
    internalId: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    dateCreated: Optional[datetime] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    owner: Optional[UserReference] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = Field(None, unique_items=True)
    references: Optional[List[ReferenceFileReference]] = None
    mtSettingsPerLanguageList: Optional[List[MTSettingsPerLanguageReference]] = None
    userRole: Optional[str] = Field(
        None, description="Response differs based on user's role"
    )


class AdminProjectManager(AbstractProjectDto):
    shared: Optional[bool] = Field(None, description="Default: false")
    progress: Optional[ProgressDto] = None
    client: Optional[ClientReference] = None
    costCenter: Optional[CostCenterReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    dateDue: Optional[datetime] = None
    status: Optional[Status2] = None
    purchaseOrder: Optional[str] = None
    isPublishedOnJobBoard: Optional[bool] = Field(None, description="Default: false")
    note: Optional[str] = None
    createdBy: Optional[UserReference] = None
    qualityAssuranceSettings: Optional[ObjectReference] = None
    workflowSteps: Optional[List[ProjectWorkflowStepDto]] = None
    analyseSettings: Optional[ObjectReference] = None
    accessSettings: Optional[ObjectReference] = None
    financialSettings: Optional[ObjectReference] = None
    archived: Optional[bool] = None


class Buyer(AbstractProjectDto):
    shared: Optional[bool] = Field(None, description="Default: false")
    progress: Optional[ProgressDto] = None
    client: Optional[ClientReference] = None
    costCenter: Optional[CostCenterReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    dateDue: Optional[datetime] = None
    status: Optional[Status3] = None
    purchaseOrder: Optional[str] = None
    isPublishedOnJobBoard: Optional[bool] = Field(None, description="Default: false")
    note: Optional[str] = None
    createdBy: Optional[UserReference] = None
    qualityAssuranceSettings: Optional[ObjectReference] = None
    workflowSteps: Optional[List[ProjectWorkflowStepDto]] = None
    analyseSettings: Optional[ObjectReference] = None
    accessSettings: Optional[ObjectReference] = None
    financialSettings: Optional[ObjectReference] = None
    archived: Optional[bool] = None
    vendorOwner: Optional[USER] = None
    vendor: Optional[VendorReference] = None


class Linguist(AbstractProjectDto):
    pass


class Vendor(AbstractProjectDto):
    shared: Optional[bool] = Field(None, description="Default: false")
    progress: Optional[ProgressDto] = None
    client: Optional[ClientReference] = None
    costCenter: Optional[CostCenterReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    dateDue: Optional[datetime] = None
    status: Optional[Status4] = None
    purchaseOrder: Optional[str] = None
    isPublishedOnJobBoard: Optional[bool] = Field(None, description="Default: false")
    note: Optional[str] = None
    createdBy: Optional[UserReference] = None
    qualityAssuranceSettings: Optional[ObjectReference] = None
    workflowSteps: Optional[List[ProjectWorkflowStepDto]] = None
    analyseSettings: Optional[ObjectReference] = None
    accessSettings: Optional[ObjectReference] = None
    financialSettings: Optional[ObjectReference] = None
    archived: Optional[bool] = None
    buyerOwner: Optional[USER] = None
    buyer: Optional[BuyerReference] = None


class PageDtoAbstractProjectDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[AbstractProjectDto]] = None


class ProjectTemplateDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    templateName: Optional[str] = None
    name: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    note: Optional[str] = None
    useDynamicTitle: Optional[bool] = None
    dynamicTitle: Optional[str] = None
    owner: Optional[UserReference] = None
    client: Optional[ClientReference] = None
    domain: Optional[DomainReference] = None
    subDomain: Optional[SubDomainReference] = None
    vendor: Optional[VendorReference] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    modifiedBy: Optional[UserReference] = None
    dateModified: Optional[datetime] = Field(
        None,
        description="Deprecated - use dateTimeModified field instead",
        example='{ "epochSeconds": 1624619701, "nano": 0 }',
    )
    dateTimeModified: Optional[datetime] = None
    workflowSteps: Optional[List[WorkflowStepDto]] = None
    workflowSettings: Optional[List[WorkflowStepSettingsDto]] = None
    businessUnit: Optional[BusinessUnitReference] = None
    notifyProviders: Optional[ProjectTemplateNotifyProviderDto] = None
    assignedTo: Optional[List[AssignmentPerTargetLangDto]] = None
    importSettings: Optional[UidReference] = Field(
        None, description="Deprecated - always null"
    )


class LqaSettingsDto(BaseModel):
    enabled: Optional[bool] = None
    severities: Optional[List[LqaSeverityDto]] = None
    categories: Optional[List[LqaErrorCategoryDto]] = None


class PageDtoQuoteDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[QuoteDto]] = None


class JobPartExtendedDto(BaseModel):
    uid: Optional[str] = None
    innerId: Optional[str] = Field(
        None,
        description="InnerId is a sequential number of a job in a project. Jobs created from the same file share the same innerId across workflow steps.",
    )
    status: Optional[Status9] = None
    providers: Optional[List[ProviderReference]] = None
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    workflowLevel: Optional[int] = None
    workflowStep: Optional[ProjectWorkflowStepReference] = None
    filename: Optional[str] = None
    dateDue: Optional[datetime] = None
    wordsCount: Optional[int] = None
    beginIndex: Optional[int] = None
    endIndex: Optional[int] = None
    isParentJobSplit: Optional[bool] = None
    updateSourceDate: Optional[datetime] = None
    updateTargetDate: Optional[datetime] = None
    dateCreated: Optional[datetime] = None
    jobReference: Optional[JobReference] = None
    project: Optional[ProjectReference] = None
    lastWorkflowLevel: Optional[int] = None
    workUnit: Optional[ObjectReference] = None
    importStatus: Optional[ImportStatusDto] = None
    imported: Optional[bool] = None
    continuous: Optional[bool] = None
    continuousJobInfo: Optional[ContinuousJobInfoDto] = None
    originalFileDirectory: Optional[str] = None


class PseudoTranslateActionDto(BaseModel):
    replacement: constr(min_length=1, max_length=10)
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    length: Optional[float] = None
    keyHashPrefixLen: Optional[conint(ge=0, le=18)] = None
    substitution: List[SubstituteDto] = Field(..., max_items=100, min_items=1)


class JobSegmentDto(BaseModel):
    id: Optional[str] = None
    source: Optional[str] = None
    translation: Optional[str] = None
    createdAt: Optional[int] = None
    modifiedAt: Optional[int] = None
    createdBy: Optional[UserReference] = None
    modifiedBy: Optional[UserReference] = None
    workflowLevel: Optional[int] = None
    workflowStep: Optional[WorkflowStepDto] = None


class SegmentListDto(BaseModel):
    segments: Optional[List[JobSegmentDto]] = None


class JobListDto(BaseModel):
    unsupportedFiles: Optional[List[str]] = None
    jobs: Optional[List[JobPartReference]] = None
    asyncRequest: Optional[AsyncRequestReference] = None


class ProvidersPerLanguage(BaseModel):
    targetLang: Optional[str] = None
    providers: Optional[List[ProviderReference]] = None
    assignedUsers: Optional[List[User]] = None


class WorkflowStepConfiguration(BaseModel):
    id: Optional[str] = None
    assignments: List[ProvidersPerLanguage]
    due: Optional[datetime] = Field(None, description="Use ISO 8601 date format.")
    notifyProvider: Optional[NotifyProviderDto] = None


class UpdateIgnoredSegment(BaseModel):
    uid: str
    warnings: List[UpdateIgnoredWarning] = Field(..., max_items=100, min_items=1)


class UpdateIgnoredWarningsDto(BaseModel):
    segments: List[UpdateIgnoredSegment] = Field(..., max_items=500, min_items=1)


class SearchJobsDto(BaseModel):
    jobs: Optional[List[JobPartExtendedDto]] = None


class PreviousWorkflowDto(BaseModel):
    completed: Optional[bool] = None
    counts: Optional[SegmentsCountsDto] = None


class SegmentsCountsResponseDto(BaseModel):
    jobPartUid: Optional[str] = None
    counts: Optional[SegmentsCountsDto] = None
    previousWorkflow: Optional[PreviousWorkflowDto] = None


class SegmentsCountsResponseListDto(BaseModel):
    segmentsCountsResults: Optional[List[SegmentsCountsResponseDto]] = None


class CreateTermsDto(BaseModel):
    sourceTerm: TermCreateByJobDto
    targetTerm: TermCreateByJobDto


class SearchResponseListTbDto(BaseModel):
    searchResults: Optional[List[SearchResponseTbDto]] = None


class PageDtoTransMemoryDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[TransMemoryDto]] = None


class ProjectTemplateEditDto(BaseModel):
    name: Optional[constr(min_length=0, max_length=255)] = None
    templateName: constr(min_length=0, max_length=255)
    sourceLang: Optional[str] = None
    targetLangs: Optional[List[str]] = None
    useDynamicTitle: Optional[bool] = None
    dynamicTitle: Optional[constr(min_length=0, max_length=255)] = None
    notifyProvider: Optional[ProjectTemplateNotifyProviderDto] = Field(
        None,
        description="use to notify assigned providers,\n        notificationIntervalInMinutes 0 or empty value means immediate notification to all providers",
    )
    workFlowSettings: Optional[List[WorkflowStepSettingsEditDto]] = None
    client: Optional[IdReference] = None
    costCenter: Optional[IdReference] = None
    businessUnit: Optional[IdReference] = None
    domain: Optional[IdReference] = None
    subDomain: Optional[IdReference] = None
    vendor: Optional[IdReference] = None
    importSettings: Optional[UidReference] = None
    note: Optional[constr(min_length=0, max_length=4096)] = None
    fileHandover: Optional[bool] = Field(None, description="Default: false")
    assignedTo: Optional[List[ProjectTemplateWorkflowSettingsAssignedToDto]] = Field(
        None,
        description="only use for projects without workflows; otherwise specify in the workflowSettings object",
    )


class PageDtoProjectTemplateReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[ProjectTemplateReference]] = None


class ServiceProviderConfigDto(BaseModel):
    authenticationSchemes: Optional[List[AuthSchema]] = None
    schemas: Optional[List[str]] = None
    patch: Optional[Supported] = None
    bulk: Optional[Supported] = None
    filter: Optional[Supported] = None
    changePassword: Optional[Supported] = None
    sort: Optional[Supported] = None
    etag: Optional[Supported] = None
    xmlDataFormat: Optional[Supported] = None


class PageDtoSegmentationRuleReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[SegmentationRuleReference]] = None


class CheckResponse(BaseModel):
    text: Optional[str] = None
    misspelledWords: Optional[List[MisspelledWord]] = None


class SpellCheckResponseDto(BaseModel):
    spellCheckResults: Optional[List[CheckResponse]] = None


class SuggestResponse(BaseModel):
    word: Optional[str] = None
    suggestions: Optional[List[Suggestion]] = None


class SuggestResponseDto(BaseModel):
    suggestResults: Optional[List[SuggestResponse]] = None


class PageDtoSubDomainDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[SubDomainDto]] = None


class ConceptListResponseDto(BaseModel):
    concepts: Optional[List[ConceptWithMetadataDto]] = None
    totalCount: Optional[int] = None


class MetadataResponse(BaseModel):
    segmentsCount: Optional[int] = None
    deduplicatedSegmentsCount: Optional[int] = None
    metadataByLanguage: Optional[Dict[str, LanguageMetadata1]] = None


class AsyncExportTMByQueryDto(BaseModel):
    asyncRequest: Optional[ObjectReference] = None
    transMemory: Optional[ObjectReference] = None
    exportTargetLangs: Optional[List[str]] = None
    queries: Optional[List[Query]] = None


class TranslationPriceListDto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    dateCreated: Optional[datetime] = None
    name: str
    currencyCode: Optional[str] = None
    billingUnit: Optional[BillingUnit1] = None
    priceSets: Optional[List[TranslationPriceSetDto]] = None


class PageDtoTranslationPriceListDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[TranslationPriceListDto]] = None


class PageDtoProjectReference(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[ProjectReference]] = None


class AssignedJobDto(BaseModel):
    uid: Optional[str] = None
    innerId: Optional[str] = None
    filename: Optional[str] = None
    dateDue: Optional[datetime] = None
    dateCreated: Optional[datetime] = None
    status: Optional[Status21] = None
    targetLang: Optional[str] = None
    sourceLang: Optional[str] = None
    project: Optional[ProjectReference] = None
    workflowStep: Optional[ProjectWorkflowStepReference] = None
    importStatus: Optional[ImportStatusDto] = None
    imported: Optional[bool] = None


class PageDtoAssignedJobDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[AssignedJobDto]] = None


class PageDtoWebhookCallDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[WebhookCallDto]] = None


class DataDto(BaseModel):
    available: Optional[bool] = None
    estimate: Optional[bool] = None
    all: Optional[CountsDto] = None
    repetitions: Optional[CountsDto] = None
    transMemoryMatches: Optional[MatchCounts101Dto] = None
    machineTranslationMatches: Optional[MatchCountsDto] = None
    nonTranslatablesMatches: Optional[MatchCountsNTDto] = None
    internalFuzzyMatches: Optional[MatchCountsDto] = None


class AsyncResponseV2Dto(BaseModel):
    dateCreated: Optional[datetime] = None
    errorCode: Optional[str] = None
    errorDesc: Optional[str] = None
    errorDetails: Optional[List[ErrorDetailDtoV2]] = None
    warnings: Optional[List[ErrorDetailDtoV2]] = None


class AdminProjectManagerV2(AbstractProjectDtoV2):
    shared: Optional[bool] = Field(None, description="Default: false")
    progress: Optional[ProgressDtoV2] = None
    client: Optional[ClientReference] = None
    costCenter: Optional[CostCenterReference] = None
    businessUnit: Optional[BusinessUnitReference] = None
    dateDue: Optional[datetime] = None
    status: Optional[Status22] = None
    purchaseOrder: Optional[str] = None
    isPublishedOnJobBoard: Optional[bool] = Field(None, description="Default: false")
    note: Optional[str] = None
    createdBy: Optional[UserReference] = None
    qualityAssuranceSettings: Optional[ObjectReference] = None
    workflowSteps: Optional[List[ProjectWorkflowStepDtoV2]] = None
    analyseSettings: Optional[ObjectReference] = None
    accessSettings: Optional[ObjectReference] = None
    financialSettings: Optional[ObjectReference] = None


class ProjectWorkflowStepListDtoV2(BaseModel):
    projectWorkflowSteps: Optional[List[ProjectWorkflowStepDtoV2]] = None


class PseudoTranslateActionDtoV2(BaseModel):
    replacement: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    length: Optional[float] = None
    keyHashPrefixLen: Optional[conint(ge=0, le=18)] = None
    substitution: Optional[List[SubstituteDtoV2]] = Field(
        None, max_items=2147483647, min_items=0
    )


class PseudoTranslateWrapperDto(BaseModel):
    jobParts: JobPartReadyReferences
    pseudoTranslate: PseudoTranslateActionDtoV2


class JobPartReadyDeleteTranslationDto(BaseModel):
    jobs: List[UidReference] = Field(..., max_items=100, min_items=1)
    deleteSettings: Optional[TranslationSegmentsReferenceV2] = None
    forAllJobs: Optional[bool] = Field(
        None,
        description="Set true if you want to delete translations for all jobs from project from specific workflow step.\n               Default: false",
    )
    workflowLevel: Optional[int] = Field(
        None, description="Specifies workflow level for all jobs"
    )
    getParts: Optional[Dict[str, Any]] = None


class ProjectTemplateTransMemoryListV2Dto(BaseModel):
    transMemories: Optional[List[ProjectTemplateTransMemoryV2Dto]] = None


class SetContextPTTransMemoriesV2Dto(BaseModel):
    transMemories: List[SetProjectTemplateTransMemoryV2Dto]
    targetLang: Optional[str] = Field(
        None,
        description="Set translation memory only for the specific project target language",
    )
    workflowStep: Optional[UidReference] = Field(
        None, description="Set translation memory only for the specific workflow step"
    )
    orderEnabled: Optional[bool] = Field(None, description="Default: false")


class SetProjectTemplateTransMemoriesV2Dto(BaseModel):
    dataPerContext: List[SetContextPTTransMemoriesV2Dto]


class QuoteCreateV2Dto(BaseModel):
    name: constr(min_length=0, max_length=255)
    project: UidReference
    analyse: IdReference
    priceList: IdReference
    netRateScheme: Optional[IdReference] = None
    provider: Optional[ProviderReference] = None
    workflowSettings: Optional[List[QuoteWorkflowSettingDto]] = Field(
        None, unique_items=True
    )
    units: Optional[List[QuoteUnitsDto]] = None


class SearchTbResponseDto(BaseModel):
    termBase: Optional[TermBaseReference] = None
    concept: Optional[ConceptDtov2] = None
    sourceTerm: Optional[TermV2Dto] = None
    translationTerms: Optional[List[TermV2Dto]] = None


class SearchTbResponseListDto(BaseModel):
    searchResults: Optional[List[SearchTbResponseDto]] = None


class AnalyseLanguagePartV3Dto(BaseModel):
    id: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    data: Optional[DataDto] = None
    discountedData: Optional[DataDto] = None
    jobs: Optional[List[AnalyseJobReference]] = None
    transMemories: Optional[List[TransMemoryReferenceDtoV2]] = None


class AnalyseV3Dto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    innerId: Optional[int] = None
    type: Optional[Type15] = None
    name: Optional[str] = None
    provider: Optional[ProviderReference] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    netRateScheme: Optional[NetRateSchemeReference] = None
    canChangeNetRateScheme: Optional[bool] = None
    analyseLanguageParts: Optional[List[AnalyseLanguagePartV3Dto]] = None
    settings: Optional[AbstractAnalyseSettingsDto] = None
    outdated: Optional[bool] = None
    importStatus: Optional[ImportStatusDto] = None
    pureWarnings: Optional[List[str]] = None
    project: Optional[ProjectReference] = None


class SearchTMSegmentDtoV3(BaseModel):
    id: Optional[str] = None
    text: Optional[str] = None
    lang: Optional[str] = None
    rtl: Optional[bool] = None
    modifiedAt: Optional[int] = None
    createdAt: Optional[int] = None
    modifiedBy: Optional[UserReference] = None
    createdBy: Optional[UserReference] = None
    filename: Optional[str] = None
    project: Optional[SearchTMProjectDtoV3] = None
    client: Optional[SearchTMClientDtoV3] = None
    domain: Optional[SearchTMDomainDtoV3] = None
    subDomain: Optional[SearchTMSubDomainDtoV3] = None
    tagMetadata: Optional[List[TagMetadata]] = None
    previousSegment: Optional[str] = None
    nextSegment: Optional[str] = None
    key: Optional[str] = None
    targetNote: Optional[str] = None


class AbsoluteTranslationLengthWarningDto(SegmentWarning):
    limit: Optional[str] = None


class EmptyPairTagsWarningDto(SegmentWarning):
    pass


class EmptyTagContentWarningDto(SegmentWarning):
    pass


class EmptyTranslationWarningDto(SegmentWarning):
    pass


class ExtraNumbersV3WarningDto(SegmentWarning):
    number: Optional[str] = None
    positions: Optional[List[Position]] = None


class ExtraNumbersWarningDto(SegmentWarning):
    extraNumbers: Optional[List[str]] = None


class ForbiddenStringWarningDto(SegmentWarning):
    forbiddenString: Optional[str] = None
    positions: Optional[List[Position]] = None


class ForbiddenTermWarningDto(SegmentWarning):
    term: Optional[str] = None
    positions: Optional[List[Position]] = None
    sourceTerms: Optional[List[Term]] = None


class FormattingWarningDto(SegmentWarning):
    pass


class InconsistentTagContentWarningDto(SegmentWarning):
    pass


class InconsistentTranslationWarningDto(SegmentWarning):
    segmentId: Optional[str] = None


class JoinTagsWarningDto(SegmentWarning):
    sourceTagsCount: Optional[int] = None
    translationTagsCount: Optional[int] = None


class LeadingAndTrailingSpacesWarningDto(SegmentWarning):
    srcPosition: Optional[Position] = None
    srcWhitespaces: Optional[str] = None
    tgtPosition: Optional[Position] = None
    tgtWhitespaces: Optional[str] = None
    suggestion: Optional[Suggestion] = None


class MalformedWarningDto(SegmentWarning):
    message: Optional[str] = None


class MissingNumbersV3WarningDto(SegmentWarning):
    number: Optional[str] = None
    positions: Optional[List[Position]] = None


class MissingNumbersWarningDto(SegmentWarning):
    missingNumbers: Optional[List[str]] = None


class MoraviaWarningDto(SegmentWarning):
    message: Optional[str] = None
    subType: Optional[str] = None


class MultipleSpacesV3WarningDto(SegmentWarning):
    spaces: Optional[str] = None
    positions: Optional[List[Position]] = None


class MultipleSpacesWarningDto(SegmentWarning):
    pass


class NestedTagsWarningDto(SegmentWarning):
    misplacedTargetTag: Optional[str] = None


class NewerAtLowerLevelWarningDto(SegmentWarning):
    pass


class NonConformingTermWarningDto(SegmentWarning):
    term: Optional[str] = None
    positions: Optional[List[Position]] = None
    suggestedTargetTerms: Optional[List[Term]] = None


class NotConfirmedWarningDto(SegmentWarning):
    pass


class RelativeTranslationLengthWarningDto(SegmentWarning):
    limit: Optional[str] = None


class RepeatedWordWarningDto(SegmentWarning):
    word: Optional[str] = None
    positions: Optional[List[Position]] = None


class RepeatedWordsWarningDto(SegmentWarning):
    repeatedWords: Optional[List[str]] = None


class SegmentWarningsDto(BaseModel):
    segmentId: Optional[str] = None
    warnings: Optional[List[SegmentWarning]] = None
    ignoredChecks: Optional[List[str]] = None


class SourceTargetRegexpWarningDto(SegmentWarning):
    description: Optional[str] = None


class SpellCheckWarningDto(SegmentWarning):
    misspelledWords: Optional[List[MisspelledWordDto]] = None


class TargetSourceIdenticalWarningDto(SegmentWarning):
    pass


class TerminologyWarningDto(SegmentWarning):
    missingTerms: Optional[List[str]] = None
    forbiddenTerms: Optional[List[str]] = None


class TrailingPunctuationWarningDto(SegmentWarning):
    srcPosition: Optional[Position] = None
    srcEndPunctuation: Optional[str] = None
    tgtPosition: Optional[Position] = None
    tgtEndPunctuation: Optional[str] = None


class TrailingSpaceWarningDto(SegmentWarning):
    pass


class TranslationLengthWarningDto(SegmentWarning):
    pass


class UnmodifiedFuzzyTranslationMTNTWarningDto(SegmentWarning):
    transOrigin: Optional[str] = None


class UnmodifiedFuzzyTranslationTMWarningDto(SegmentWarning):
    transOrigin: Optional[str] = None


class UnmodifiedFuzzyTranslationWarningDto(SegmentWarning):
    transOrigin: Optional[str] = None


class UnresolvedCommentWarningDto(SegmentWarning):
    pass


class UnresolvedConversationWarningDto(SegmentWarning):
    pass


class ProjectTemplateTransMemoryDtoV3(BaseModel):
    targetLocale: Optional[str] = None
    workflowStep: Optional[WorkflowStepReferenceV3] = None
    readMode: Optional[bool] = None
    writeMode: Optional[bool] = None
    transMemory: Optional[TransMemoryDtoV3] = None
    penalty: Optional[float] = None
    applyPenaltyTo101Only: Optional[bool] = None


class ProjectTemplateTransMemoryListDtoV3(BaseModel):
    transMemories: Optional[List[ProjectTemplateTransMemoryDtoV3]] = None


class SetContextTransMemoriesDtoV3Dto(BaseModel):
    transMemories: List[SetProjectTransMemoryV3Dto]
    targetLang: Optional[str] = Field(
        None,
        description="Set translation memory only for the specific project target language",
    )
    workflowStep: Optional[UidReference] = Field(
        None, description="Set translation memory only for the specific workflow step"
    )
    orderEnabled: Optional[bool] = Field(None, description="Default: false")


class SetProjectTransMemoriesV3Dto(BaseModel):
    dataPerContext: List[SetContextTransMemoriesDtoV3Dto]


class ADMINRESPONSE(UserDetailsDtoV3):
    pass


class GUESTRESPONSE(UserDetailsDtoV3):
    client: ClientReference
    enableMT: Optional[bool] = None
    projectViewOther: Optional[bool] = None
    projectViewOtherLinguist: Optional[bool] = None
    projectViewOtherEditor: Optional[bool] = None
    transMemoryViewOther: Optional[bool] = None
    transMemoryEditOther: Optional[bool] = None
    transMemoryExportOther: Optional[bool] = None
    transMemoryImportOther: Optional[bool] = None
    termBaseViewOther: Optional[bool] = None
    termBaseEditOther: Optional[bool] = None
    termBaseExportOther: Optional[bool] = None
    termBaseImportOther: Optional[bool] = None
    termBaseApproveOther: Optional[bool] = None


class LINGUISTRESPONSE(UserDetailsDtoV3):
    editAllTermsInTB: Optional[bool] = None
    editTranslationsInTM: Optional[bool] = None
    enableMT: Optional[bool] = None
    mayRejectJobs: Optional[bool] = None
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    workflowSteps: Optional[List[WorkflowStepReferenceV3]] = None
    clients: Optional[List[ClientReference]] = None
    domains: Optional[List[DomainReference]] = None
    subDomains: Optional[List[SubDomainReference]] = None
    netRateScheme: Optional[DiscountSchemeReference] = None
    translationPriceList: Optional[PriceListReference] = None


class PROJECTMANAGERRESPONSE(UserDetailsDtoV3):
    sourceLocales: Optional[List[str]] = None
    targetLocales: Optional[List[str]] = None
    workflowSteps: Optional[List[WorkflowStepReferenceV3]] = None
    clients: Optional[List[ClientReference]] = None
    domains: Optional[List[DomainReference]] = None
    subDomains: Optional[List[SubDomainReference]] = None
    projectCreate: Optional[bool] = None
    projectViewOther: Optional[bool] = None
    projectEditOther: Optional[bool] = None
    projectDeleteOther: Optional[bool] = None
    projectClients: Optional[List[ClientReference]] = None
    projectBusinessUnits: Optional[List[BusinessUnitReference]] = None
    projectTemplateCreate: Optional[bool] = None
    projectTemplateViewOther: Optional[bool] = None
    projectTemplateEditOther: Optional[bool] = None
    projectTemplateDeleteOther: Optional[bool] = None
    projectTemplateClients: Optional[List[ClientReference]] = None
    projectTemplateBusinessUnits: Optional[List[BusinessUnitReference]] = None
    transMemoryCreate: Optional[bool] = None
    transMemoryViewOther: Optional[bool] = None
    transMemoryEditOther: Optional[bool] = None
    transMemoryDeleteOther: Optional[bool] = None
    transMemoryExportOther: Optional[bool] = None
    transMemoryImportOther: Optional[bool] = None
    transMemoryClients: Optional[List[ClientReference]] = None
    transMemoryBusinessUnits: Optional[List[BusinessUnitReference]] = None
    termBaseCreate: Optional[bool] = None
    termBaseViewOther: Optional[bool] = None
    termBaseEditOther: Optional[bool] = None
    termBaseDeleteOther: Optional[bool] = None
    termBaseExportOther: Optional[bool] = None
    termBaseImportOther: Optional[bool] = None
    termBaseApproveOther: Optional[bool] = None
    termBaseClients: Optional[List[ClientReference]] = None
    termBaseBusinessUnits: Optional[List[BusinessUnitReference]] = None
    userCreate: Optional[bool] = None
    userViewOther: Optional[bool] = None
    userEditOther: Optional[bool] = None
    userDeleteOther: Optional[bool] = None
    clientDomainSubDomainCreate: Optional[bool] = None
    clientDomainSubDomainViewOther: Optional[bool] = None
    clientDomainSubDomainEditOther: Optional[bool] = None
    clientDomainSubDomainDeleteOther: Optional[bool] = None
    vendorCreate: Optional[bool] = None
    vendorViewOther: Optional[bool] = None
    vendorEditOther: Optional[bool] = None
    vendorDeleteOther: Optional[bool] = None
    dashboardSetting: Optional[str] = None
    setupServer: Optional[bool] = None


class SUBMITTERRESPONSE(UserDetailsDtoV3):
    automationWidgets: List[IdReference]
    projectViewCreatedByOtherSubmitters: Optional[bool] = None


class ADMINEDIT(AbstractUserEditDto):
    pass


class ADMIN(AbstractUserCreateDto):
    pass


class AsyncRequestDto(BaseModel):
    id: Optional[str] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    action: Optional[Action] = None
    asyncResponse: Optional[AsyncResponseDto] = None
    parent: Optional[AsyncRequestDto] = None
    project: Optional[ProjectReference] = None


class AnalyseLanguagePartDto(BaseModel):
    id: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    data: Optional[DataDtoV1] = None
    discountedData: Optional[DataDtoV1] = None
    jobs: Optional[List[AnalyseJobReference]] = None


class PageDtoAsyncRequestDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[AsyncRequestDto]] = None


class JobRoleDto(BaseModel):
    type: Type2
    workflowStep: Optional[ProjectWorkflowStepDtoV2] = Field(
        None,
        description="not null only for `PROVIDER` type and project with defined workflow steps",
    )
    organizationType: Optional[OrganizationType] = Field(
        None, description="not null only for shared projects"
    )


class MentionableUserDto(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    userName: Optional[str] = None
    email: Optional[str] = None
    role: Optional[Role1] = None
    id: Optional[str] = None
    uid: Optional[str] = None
    unavailable: Optional[bool] = None
    jobRoles: Optional[List[JobRoleDto]] = None


class StatusDto(BaseModel):
    name: Optional[Name] = None
    by: Optional[MentionableUserDto] = None
    date: Optional[datetime] = None


class CustomFileTypeDto(BaseModel):
    uid: Optional[str] = None
    name: Optional[str] = None
    filenamePattern: Optional[str] = None
    type: Optional[str] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    fileImportSettings: Optional[FileImportSettingsDto] = None


class PageDtoCustomFileTypeDto(BaseModel):
    totalElements: Optional[int] = None
    totalPages: Optional[int] = None
    pageSize: Optional[int] = None
    pageNumber: Optional[int] = None
    numberOfElements: Optional[int] = None
    content: Optional[List[CustomFileTypeDto]] = None


class SearchTMResponseDto(BaseModel):
    segmentId: Optional[str] = None
    source: Optional[SearchTMSegmentDto] = None
    translations: Optional[List[SearchTMSegmentDto]] = None
    transMemory: Optional[SearchTMTransMemoryDto] = None
    grossScore: Optional[float] = None
    score: Optional[float] = None
    subSegment: Optional[bool] = None


class ErrorCategoriesDto(BaseModel):
    accuracy: Optional[AccuracyWeightsDto] = None
    fluency: Optional[FluencyWeightsDto] = None
    terminology: Optional[TerminologyWeightsDto] = None
    style: Optional[StyleWeightsDto] = None
    localeConvention: Optional[LocaleConventionWeightsDto] = None
    verity: Optional[VerityWeightsDto] = None
    design: Optional[DesignWeightsDto] = None
    other: Optional[OtherWeightsDto] = None


class LqaProfileDetailDto(BaseModel):
    uid: str = Field(..., description="UID of the profile", example="string")
    name: str = Field(..., description="Name of the profile")
    errorCategories: ErrorCategoriesDto
    penaltyPoints: PenaltyPointsDto
    passFailThreshold: PassFailThresholdDto
    isDefault: bool = Field(
        ..., description="If profile is set as default for organization"
    )
    createdBy: UserReference
    dateCreated: datetime
    organization: UidReference


class UpdateLqaProfileDto(BaseModel):
    name: constr(min_length=1, max_length=255)
    errorCategories: ErrorCategoriesDto
    penaltyPoints: Optional[PenaltyPointsDto] = None
    passFailThreshold: Optional[PassFailThresholdDto] = None


class CreateLqaProfileDto(BaseModel):
    name: constr(min_length=1, max_length=255)
    errorCategories: ErrorCategoriesDto
    penaltyPoints: Optional[PenaltyPointsDto] = None
    passFailThreshold: Optional[PassFailThresholdDto] = None


class AssignableTemplatesDto(BaseModel):
    assignableTemplates: Optional[List[ProjectTemplateDto]] = None


class AsyncRequestWrapperDto(BaseModel):
    asyncRequest: Optional[AsyncRequestDto] = None


class JobCreateRequestDto(BaseModel):
    targetLangs: List[str]
    due: Optional[datetime] = Field(
        None,
        description="only use for projects without workflows; otherwise specify in the workflowSettings object. Use ISO 8601 date format.",
    )
    workflowSettings: Optional[List[WorkflowStepConfiguration]] = None
    assignments: Optional[List[ProvidersPerLanguage]] = Field(
        None,
        description="only use for projects without workflows; otherwise specify in the workflowSettings object",
    )
    importSettings: Optional[UidReference] = None
    useProjectFileImportSettings: Optional[bool] = Field(
        None, description="Default: false"
    )
    preTranslate: Optional[bool] = None
    notifyProvider: Optional[NotifyProviderDto] = Field(
        None,
        description="use to notify assigned providers, notificationIntervalInMinutes 0 or empty value means immediate notification to all providers",
    )
    callbackUrl: Optional[str] = None
    path: Optional[constr(min_length=0, max_length=255)] = None
    remoteFile: Optional[JobCreateRemoteFileDto] = None


class BackgroundTasksTbDto(BaseModel):
    status: Optional[str] = None
    finishedDataText: Optional[str] = None
    asyncRequest: Optional[AsyncRequestDto] = None
    lastTaskString: Optional[str] = None
    metadata: Optional[MetadataResponse] = None
    lastTaskOk: Optional[str] = None
    lastTaskError: Optional[str] = None
    lastTaskErrorHtml: Optional[str] = None


class BackgroundTasksTmDto(BaseModel):
    status: Optional[str] = None
    finishedDataText: Optional[str] = None
    asyncRequest: Optional[AsyncRequestDto] = None
    lastTaskString: Optional[str] = None
    metadata: Optional[MetadataResponse] = None
    lastTaskOk: Optional[str] = None
    lastTaskError: Optional[str] = None
    lastTaskErrorHtml: Optional[str] = None


class AsyncExportTMByQueryResponseDto(BaseModel):
    asyncRequest: Optional[AsyncRequestDto] = None
    asyncExport: Optional[AsyncExportTMByQueryDto] = None


class AnalyseLanguagePartV2Dto(BaseModel):
    id: Optional[str] = None
    sourceLang: Optional[str] = None
    targetLang: Optional[str] = None
    data: Optional[DataDto] = None
    discountedData: Optional[DataDto] = None
    jobs: Optional[List[AnalyseJobReference]] = None


class AnalyseV2Dto(BaseModel):
    id: Optional[str] = None
    uid: Optional[str] = None
    type: Optional[Type13] = None
    name: Optional[str] = None
    provider: Optional[ProviderReference] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    netRateScheme: Optional[NetRateSchemeReference] = None
    analyseLanguageParts: Optional[List[AnalyseLanguagePartV2Dto]] = None


class AsyncRequestV2Dto(BaseModel):
    id: Optional[str] = None
    createdBy: Optional[UserReference] = None
    dateCreated: Optional[datetime] = None
    action: Optional[Action2] = None
    asyncResponse: Optional[AsyncResponseV2Dto] = None
    parent: Optional[AsyncRequestV2Dto] = None
    project: Optional[ProjectReference] = None


class AnalysesV2Dto(BaseModel):
    analyses: Optional[List[AnalyseV2Dto]] = None


class AsyncRequestWrapperV2Dto(BaseModel):
    asyncRequest: Optional[AsyncRequestV2Dto] = None


class AsyncExportTMResponseDto(BaseModel):
    asyncRequest: Optional[AsyncRequestV2Dto] = None
    asyncExport: Optional[AsyncExportTMDto] = None


class SearchTMResponseDtoV3(BaseModel):
    segmentId: Optional[str] = None
    source: Optional[SearchTMSegmentDtoV3] = None
    translations: Optional[List[SearchTMSegmentDtoV3]] = None
    transMemory: Optional[SearchTMTransMemoryDtoV3] = None
    grossScore: Optional[float] = None
    score: Optional[float] = None
    subSegment: Optional[bool] = None


class QualityAssuranceResponseDto(BaseModel):
    segmentWarnings: Optional[List[SegmentWarningsDto]] = None
    finished: Optional[bool] = None


class AsyncAnalyseResponseDto(BaseModel):
    asyncRequest: Optional[AsyncRequestDto] = None
    analyse: Optional[ObjectReference] = None


class AnalyseRecalculateResponseDto(BaseModel):
    analyses: Optional[List[AsyncAnalyseResponseDto]] = None


class AsyncAnalyseListResponseDto(BaseModel):
    analyses: Optional[List[AsyncAnalyseResponseDto]] = None


class MentionDto(BaseModel):
    mentionType: str
    interaction: Interaction
    tag: Optional[str] = None
    userUids: Optional[List[MentionableUserDto]] = None
    userReferences: Optional[List[MentionableUserDto]] = None


class SearchResponseListTmDto(BaseModel):
    searchResults: Optional[List[SearchTMResponseDto]] = None


class AsyncAnalyseResponseV2Dto(BaseModel):
    asyncRequest: Optional[AsyncRequestV2Dto] = None
    analyse: Optional[ObjectReference] = None


class SearchResponseListTmDtoV3(BaseModel):
    searchResults: Optional[List[SearchTMResponseDtoV3]] = None


class CommentDto(BaseModel):
    id: Optional[str] = None
    text: Optional[str] = None
    createdByRef: Optional[MentionableUserDto] = None
    createdBy: Optional[MentionableUserDto] = None
    dateCreated: Optional[datetime] = None
    dateModified: Optional[datetime] = None
    mentions: Optional[List[MentionDto]] = None


class CommonConversationDto(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = Field(
        None, description="Field references differs based on the Conversation Type."
    )
    dateCreated: Optional[datetime] = None
    dateModified: Optional[datetime] = None
    dateEdited: Optional[datetime] = None
    createdByRef: Optional[MentionableUserDto] = None
    createdBy: Optional[MentionableUserDto] = None
    comments: Optional[List[CommentDto]] = None
    status: Optional[StatusDto] = None
    deleted: Optional[bool] = None


class ConversationListDto(BaseModel):
    conversations: Optional[List[CommonConversationDto]] = None


class LQA(CommonConversationDto):
    references: Optional[LQAReferences] = None
    lqaDescription: Optional[str] = None


class SEGMENTTARGET(CommonConversationDto):
    references: Optional[PlainReferences] = None


class LQAConversationDto(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = Field(None, description="LQA")
    dateCreated: Optional[datetime] = None
    dateModified: Optional[datetime] = None
    dateEdited: Optional[datetime] = None
    createdByRef: Optional[MentionableUserDto] = None
    createdBy: Optional[MentionableUserDto] = None
    comments: Optional[List[CommentDto]] = None
    status: Optional[StatusDto] = None
    deleted: Optional[bool] = None
    references: Optional[LQAReferences] = None
    lqaDescription: Optional[str] = None


class LQAConversationsListDto(BaseModel):
    conversations: Optional[List[LQAConversationDto]] = None


class PlainConversationDto(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = Field(None, description="SEGMENT_TARGET")
    dateCreated: Optional[datetime] = None
    dateModified: Optional[datetime] = None
    dateEdited: Optional[datetime] = None
    createdByRef: Optional[MentionableUserDto] = None
    createdBy: Optional[MentionableUserDto] = None
    comments: Optional[List[CommentDto]] = None
    status: Optional[StatusDto] = None
    deleted: Optional[bool] = None
    references: Optional[PlainReferences] = None


class PlainConversationsListDto(BaseModel):
    conversations: Optional[List[PlainConversationDto]] = None


class AsyncAnalyseListResponseV2Dto(BaseModel):
    asyncRequests: Optional[List[AsyncAnalyseResponseV2Dto]] = None


LqaErrorCategoryDto.update_forward_refs()
Attribute.update_forward_refs()
AsyncRequestDto.update_forward_refs()
AsyncRequestV2Dto.update_forward_refs()
